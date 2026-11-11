# SME Risk Detector

Flask web app that serves the notebook's best model (GradientBoosting pipeline)
and predicts SME loan risk: High, Medium or Low.

## Run locally (works in Antigravity, VS Code or any terminal)

```bash
python -m venv venv
# Windows:  venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:8000

## Deploy on Render

1. Push this folder to a GitHub repo (keep `best_model.pkl` in it).
2. On render.com choose New > Blueprint (uses `render.yaml`), or New > Web Service with:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app --workers 1 --threads 4 --timeout 120`
3. Python version is pinned to 3.13.18 (same as the notebook) through `PYTHON_VERSION` / `.python-version`.

## Files

| File | Purpose |
|---|---|
| `app.py` | Flask routes, validation, model loading |
| `best_model.pkl` | Saved scikit-learn pipeline from the notebook |
| `feature_columns.json` | Exact feature order used in training |
| `class_labels.json` | Class codes: 0 = HIGH, 1 = LOW, 2 = MEDIUM |
| `requirements.txt` | Pinned versions from the notebook |

## JSON API

`POST /api/predict` with the 12 fields as JSON returns the level, confidence and class probabilities.
`GET /healthz` is the health check.
