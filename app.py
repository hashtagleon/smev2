"""SME Risk Detector - Flask app.

Loads the scikit-learn pipeline saved from the notebook (best_model.pkl)
and serves a two-step flow: applicant form -> risk result.
Includes bilingual English & বাংলা support.

Run locally:   python app.py
Run on Render: gunicorn app:app   (see Procfile / render.yaml)
"""
import json
import os
import pickle
from pathlib import Path
from urllib.parse import urlencode

import numpy as np
import pandas as pd
import scipy.sparse as sp
from flask import (
    Flask,
    g,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)
from sklearn.base import BaseEstimator, TransformerMixin

from translations import (
    DISTRICT_MAP,
    LOCATION_MAP,
    SECTOR_MAP,
    localize,
    localize_value,
)

BASE_DIR = Path(__file__).resolve().parent


# --------------------------------------------------------------------------
# The notebook defined `ToDense` inside Colab's __main__, so the pickle refers
# to `__main__.ToDense`. Under gunicorn (or any other entry point) that name
# does not exist, so we define the same class here and point the unpickler at it.
# --------------------------------------------------------------------------
class ToDense(TransformerMixin, BaseEstimator):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_dense = X.toarray() if sp.issparse(X) else np.array(X, copy=False)
        return np.asarray(X_dense, dtype=np.float64)


class _ModelUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if name == "ToDense":
            return ToDense
        return super().find_class(module, name)


def load_model(path):
    with open(path, "rb") as fh:
        return _ModelUnpickler(fh).load()


MODEL = load_model(BASE_DIR / "best_model.pkl")
FEATURES = json.loads((BASE_DIR / "feature_columns.json").read_text())
CLASS_CODES = json.loads((BASE_DIR / "class_labels.json").read_text())  # [0, 1, 2]

# Alphabetical sorting from training: HIGH=0, LOW=1, MEDIUM=2.
CODE_TO_LEVEL = {0: "high", 1: "low", 2: "medium"}

# Dropdown options from one-hot encoder
_cat_cols = dict(
    (name, cols) for name, _, cols in MODEL.named_steps["pre"].transformers_ if name == "cat"
)
_onehot = MODEL.named_steps["pre"].named_transformers_["cat"].named_steps["onehot"]
CATEGORIES = {col: [str(v) for v in cats] for col, cats in zip(_cat_cols["cat"], _onehot.categories_)}


# --------------------------------------------------------------------------
# Field definitions
# --------------------------------------------------------------------------
NUMERIC_FIELDS = {
    # name: (type, min, max)
    "business_age_years": (int, 0, 100),
    "owner_experience_years": (int, 0, 80),
    "banking_years": (int, 0, 80),
    "annual_revenue": (float, 1, 1e12),
    "loan_amount": (float, 1, 1e12),
    "debt_to_asset_ratio": (float, 0, 2),
    "num_employees": (int, 0, 100000),
    "collateral_value": (float, 0, 1e12),
    "past_defaults": (int, 0, 50),
}
LABELS = {
    "district": "field_district",
    "location_type": "field_location_type",
    "sector": "field_sector",
    "business_age_years": "field_business_age",
    "owner_experience_years": "field_owner_exp",
    "banking_years": "field_banking_years",
    "annual_revenue": "field_annual_rev",
    "loan_amount": "field_loan_amount",
    "debt_to_asset_ratio": "field_debt_asset",
    "num_employees": "field_employees",
    "collateral_value": "field_collateral",
    "past_defaults": "field_defaults",
}


def parse_form(data):
    """Return (clean_values, errors). Errors are keyed by field name."""
    values, errors = {}, {}
    lang = getattr(g, "lang", "en")
    for col in FEATURES:
        raw = (data.get(col) or "").strip()
        if col in CATEGORIES:
            if raw not in CATEGORIES[col]:
                field_name = localize(LABELS[col], lang)
                errors[col] = f"{localize('choose_one', lang)} {field_name}."
            else:
                values[col] = raw
            continue

        kind, lo, hi = NUMERIC_FIELDS[col]
        if raw == "":
            errors[col] = "আবশ্যক।" if lang == "bn" else "Required."
            continue
        try:
            num = float(raw.replace(",", ""))
            if not np.isfinite(num):
                raise ValueError
            if kind is int and num != int(num):
                errors[col] = "পূর্ণ সংখ্যা দিন।" if lang == "bn" else "Use a whole number."
                continue
        except ValueError:
            errors[col] = "সঠিক সংখ্যা দিন।" if lang == "bn" else "Enter a number."
            continue
        if num < lo or num > hi:
            if col == "debt_to_asset_ratio":
                errors[col] = "০ থেকে ২ এর মধ্যে হতে হবে।" if lang == "bn" else "Must be between 0 and 2."
            elif num < lo:
                errors[col] = "ঋণাত্মক হতে পারবে না।" if lang == "bn" else "Cannot be negative."
            else:
                errors[col] = "মানটি অতিরিক্ত বড়।" if lang == "bn" else "That value is too large."
            continue
        values[col] = int(num) if kind is int else float(num)
    return values, errors


def predict(values):
    row = pd.DataFrame([values], columns=FEATURES)
    probs = MODEL.predict_proba(row)[0]
    classes = [int(c) for c in MODEL.named_steps["clf"].classes_]
    by_level = {CODE_TO_LEVEL[c]: float(p) for c, p in zip(classes, probs)}
    level = max(by_level, key=by_level.get)
    return {
        "level": level,
        "confidence": by_level[level],
        "probabilities": by_level,
        "scale_position": by_level["medium"] * 0.5 + by_level["high"],
    }


def ratios(values):
    loan = values["loan_amount"]
    revenue = values["annual_revenue"]
    collateral = values["collateral_value"]
    return {
        "loan_to_revenue": loan / revenue if revenue else None,
        "collateral_cover": collateral / loan if loan else None,
    }


# --------------------------------------------------------------------------
# Demo presets
# --------------------------------------------------------------------------
PRESETS = {
    "high": {
        "title": "Leveraged textile unit",
        "title_bn": "উচ্চ ঋণগ্রস্ত টেক্সটাইল কারখানা",
        "values": dict(district="Khulna", location_type="semi_urban", sector="textiles",
                       business_age_years=2, owner_experience_years=20, banking_years=3,
                       annual_revenue=5850000, loan_amount=2140000, debt_to_asset_ratio=1.21,
                       num_employees=11, collateral_value=0, past_defaults=0),
    },
    "medium": {
        "title": "Established trading shop",
        "title_bn": "প্রতিষ্ঠিত ট্রেডিং শপ",
        "values": dict(district="Sylhet", location_type="urban", sector="trading",
                       business_age_years=16, owner_experience_years=2, banking_years=7,
                       annual_revenue=3600000, loan_amount=1690000, debt_to_asset_ratio=0.69,
                       num_employees=24, collateral_value=510000, past_defaults=0),
    },
    "low": {
        "title": "Secured agro business",
        "title_bn": "সুরক্ষিত কৃষি ব্যবসা",
        "values": dict(district="Khulna", location_type="rural", sector="agriculture",
                       business_age_years=13, owner_experience_years=9, banking_years=5,
                       annual_revenue=6400000, loan_amount=2920000, debt_to_asset_ratio=0.58,
                       num_employees=8, collateral_value=3580000, past_defaults=0),
    },
}
for _key, _preset in PRESETS.items():
    _preset["result"] = predict(_preset["values"])


# --------------------------------------------------------------------------
# App & Context Processors
# --------------------------------------------------------------------------
app = Flask(__name__)


@app.before_request
def detect_language():
    lang = request.args.get("lang") or request.cookies.get("sme_lang") or "en"
    if lang not in ("en", "bn"):
        lang = "en"
    g.lang = lang


@app.context_processor
def inject_locale_tools():
    lang = getattr(g, "lang", "en")
    return {
        "lang": lang,
        "t": lambda key, **kw: localize(key, lang, **kw),
        "loc_val": lambda val, col: localize_value(val, col, lang),
    }


@app.template_filter("pretty")
def pretty_filter(value):
    lang = getattr(g, "lang", "en")
    val_str = str(value)
    if val_str in SECTOR_MAP:
        return SECTOR_MAP[val_str].get(lang, val_str.capitalize())
    if val_str in LOCATION_MAP:
        return LOCATION_MAP[val_str].get(lang, val_str.capitalize())
    if val_str in DISTRICT_MAP and lang == "bn":
        return DISTRICT_MAP[val_str]
    text = val_str.replace("_", " ").capitalize()
    return "Semi-urban" if text == "Semi urban" else text


@app.template_filter("pct")
def pct_filter(value, digits=1):
    if value is None:
        return "N/A"
    return f"{value * 100:.{digits}f}%"


@app.template_filter("num")
def num_filter(value):
    if value is None:
        return "N/A"
    if isinstance(value, float) and value != int(value):
        return f"{value:,.2f}"
    return f"{int(value):,}"


def form_context(values=None, errors=None):
    return {
        "categories": CATEGORIES,
        "presets": PRESETS,
        "values": values or {},
        "errors": errors or {},
        "labels": LABELS,
    }


# --------------------------------------------------------------------------
# Routes
# --------------------------------------------------------------------------
@app.get("/set-language/<lang>")
def set_language(lang):
    if lang not in ("en", "bn"):
        lang = "en"
    next_url = request.args.get("next") or request.referrer or url_for("index")
    resp = redirect(next_url)
    resp.set_cookie("sme_lang", lang, max_age=30 * 86400, samesite="Lax")
    return resp


@app.get("/")
def index():
    values = {k: request.args[k] for k in FEATURES if k in request.args}
    return render_template("index.html", **form_context(values))


@app.post("/predict")
def predict_page():
    values, errors = parse_form(request.form)
    if errors:
        return render_template("index.html", **form_context(dict(request.form), errors)), 400
    result = predict(values)
    edit_url = url_for("index") + "?" + urlencode(values)
    return render_template(
        "result.html",
        values=values,
        result=result,
        ratios=ratios(values),
        labels=LABELS,
        edit_url=edit_url,
        demo=None,
    )


@app.get("/demo/<key>")
def demo(key):
    preset = PRESETS.get(key)
    if preset is None:
        return redirect(url_for("index"))
    values = preset["values"]
    lang = getattr(g, "lang", "en")
    demo_title = preset["title_bn"] if lang == "bn" else preset["title"]
    edit_url = url_for("index") + "?" + urlencode(values)
    return render_template(
        "result.html",
        values=values,
        result=preset["result"],
        ratios=ratios(values),
        labels=LABELS,
        edit_url=edit_url,
        demo=demo_title,
    )


@app.post("/api/predict")
def api_predict():
    payload = request.get_json(silent=True) or {}
    values, errors = parse_form({k: str(v) for k, v in payload.items()})
    if errors:
        return jsonify({"ok": False, "errors": errors}), 400
    res = predict(values)
    return jsonify({
        "ok": True,
        **res,
        "ratios": ratios(values)
    })


@app.get("/healthz")
def healthz():
    return jsonify(status="ok")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(host="127.0.0.1" if "PORT" not in os.environ else "0.0.0.0", port=port, debug=debug)
