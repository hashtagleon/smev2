"""SME Risk Detector - Flask app.

Loads the scikit-learn pipeline saved from the notebook (best_model.pkl)
and serves a two-step flow: applicant form -> risk result.

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
from flask import Flask, jsonify, redirect, render_template, request, url_for
from sklearn.base import BaseEstimator, TransformerMixin

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

# The notebook used LabelEncoder on risk_level, which sorts alphabetically:
# HIGH=0, LOW=1, MEDIUM=2.
CODE_TO_LEVEL = {0: "high", 1: "low", 2: "medium"}

# Dropdown options come straight from the fitted one-hot encoder,
# so the form can never offer a value the model has not seen.
_cat_cols = dict(
    (name, cols) for name, _, cols in MODEL.named_steps["pre"].transformers_ if name == "cat"
)
_onehot = MODEL.named_steps["pre"].named_transformers_["cat"].named_steps["onehot"]
CATEGORIES = {col: [str(v) for v in cats] for col, cats in zip(_cat_cols["cat"], _onehot.categories_)}


def pretty(value):
    text = str(value).replace("_", " ").capitalize()
    return "Semi-urban" if text == "Semi urban" else text


# --------------------------------------------------------------------------
# Field definitions: one place that drives both validation and the form.
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
    "district": "District",
    "location_type": "Location type",
    "sector": "Sector",
    "business_age_years": "Business age",
    "owner_experience_years": "Owner experience",
    "banking_years": "Banking relationship",
    "annual_revenue": "Annual revenue",
    "loan_amount": "Loan amount",
    "debt_to_asset_ratio": "Debt-to-asset ratio",
    "num_employees": "Employees",
    "collateral_value": "Collateral value",
    "past_defaults": "Past defaults",
}


def parse_form(data):
    """Return (clean_values, errors). Errors are keyed by field name."""
    values, errors = {}, {}
    for col in FEATURES:
        raw = (data.get(col) or "").strip()
        if col in CATEGORIES:
            if raw not in CATEGORIES[col]:
                errors[col] = f"Choose a {LABELS[col].lower()}."
            else:
                values[col] = raw
            continue

        kind, lo, hi = NUMERIC_FIELDS[col]
        if raw == "":
            errors[col] = "Required."
            continue
        try:
            num = float(raw.replace(",", ""))
            if not np.isfinite(num):
                raise ValueError
            if kind is int and num != int(num):
                errors[col] = "Use a whole number."
                continue
        except ValueError:
            errors[col] = "Enter a number."
            continue
        if num < lo or num > hi:
            if col == "debt_to_asset_ratio":
                errors[col] = "Must be between 0 and 2."
            elif num < lo:
                errors[col] = "Cannot be negative." if lo == 0 else "Must be above zero."
            else:
                errors[col] = "That value is too large."
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
        # Where the needle sits on the Low -> High scale (0 = low, 1 = high),
        # weighted by the three class probabilities.
        "scale_position": by_level["medium"] * 0.5 + by_level["high"],
    }


def ratios(values):
    loan, revenue, collateral = values["loan_amount"], values["annual_revenue"], values["collateral_value"]
    return {
        "loan_to_revenue": loan / revenue if revenue else None,
        "collateral_cover": collateral / loan if loan else None,
    }


# --------------------------------------------------------------------------
# Demo applicants. Inputs are fixed; the probabilities shown next to them are
# computed by the real model when the app starts, never hard-coded.
# --------------------------------------------------------------------------
PRESETS = {
    "high": {
        "title": "Leveraged textile unit",
        "values": dict(district="Khulna", location_type="semi_urban", sector="textiles",
                       business_age_years=2, owner_experience_years=20, banking_years=3,
                       annual_revenue=5850000, loan_amount=2140000, debt_to_asset_ratio=1.21,
                       num_employees=11, collateral_value=0, past_defaults=0),
    },
    "medium": {
        "title": "Established trading shop",
        "values": dict(district="Sylhet", location_type="urban", sector="trading",
                       business_age_years=16, owner_experience_years=2, banking_years=7,
                       annual_revenue=3600000, loan_amount=1690000, debt_to_asset_ratio=0.69,
                       num_employees=24, collateral_value=510000, past_defaults=0),
    },
    "low": {
        "title": "Secured agro business",
        "values": dict(district="Khulna", location_type="rural", sector="agriculture",
                       business_age_years=13, owner_experience_years=9, banking_years=5,
                       annual_revenue=6400000, loan_amount=2920000, debt_to_asset_ratio=0.58,
                       num_employees=8, collateral_value=3580000, past_defaults=0),
    },
}
for _key, _preset in PRESETS.items():
    _preset["result"] = predict(_preset["values"])


# --------------------------------------------------------------------------
# App
# --------------------------------------------------------------------------
app = Flask(__name__)
app.jinja_env.filters["pretty"] = pretty


@app.template_filter("pct")
def pct(value, digits=1):
    return f"{value * 100:.{digits}f}%"


@app.template_filter("num")
def num(value):
    if isinstance(value, float) and value != int(value):
        return f"{value:,.2f}"
    return f"{int(value):,}"


def form_context(values=None, errors=None):
    return {
        "categories": CATEGORIES,
        "presets": PRESETS,
        "values": values or {},
        "errors": errors or {},
    }


@app.get("/")
def index():
    # Prefill when coming back from the result page ("Edit this entry").
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
        "result.html", values=values, result=result, ratios=ratios(values),
        labels=LABELS, edit_url=edit_url, demo=None,
    )


@app.get("/demo/<key>")
def demo(key):
    preset = PRESETS.get(key)
    if preset is None:
        return redirect(url_for("index"))
    values = preset["values"]
    return render_template(
        "result.html", values=values, result=preset["result"], ratios=ratios(values),
        labels=LABELS, edit_url=url_for("index") + "?" + urlencode(values), demo=preset["title"],
    )


@app.post("/api/predict")
def api_predict():
    payload = request.get_json(silent=True) or {}
    values, errors = parse_form({k: str(v) for k, v in payload.items()})
    if errors:
        return jsonify({"ok": False, "errors": errors}), 400
    return jsonify({"ok": True, **predict(values)})


@app.get("/healthz")
def healthz():
    return jsonify(status="ok")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(host="127.0.0.1" if "PORT" not in os.environ else "0.0.0.0", port=port, debug=debug)
