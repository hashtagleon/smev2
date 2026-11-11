# SME Risk Detector

Institutional-grade SME credit risk appraisal and underwriting decision platform powered by machine learning (Gradient Boosting pipeline).

## ✨ Key Features

1. **Predictive Risk Classification**: Predicts calibrated credit risk level (**Low**, **Medium**, or **High**) with confidence score and class probability distributions.
2. **5-Pillar Credit Radar & Solvency Metrics**: Pure SVG radar visualization analyzing Stability, Leverage, Collateral Security, Banking Trust, and Credit Discipline, alongside LTV, Loan-to-Revenue, and Employee Productivity ratios.
3. **Bilingual Support (English & বাংলা)**: Instant seamless language toggle across forms, metrics, hints, and credit memos.
4. **Portfolio Analytics & Audit Database**: Embedded SQLite database (`sme_records.db`) logging all assessments, featuring real-time KPI metrics, sector exposure tables, district distribution, and one-click CSV export.
5. **AI Executive Credit Memo**: Automated narrative synthesis generating institutional credit appraisal paragraphs, key positive indicators, critical risk alerts, and underwriter policy recommendations.

## Run locally (Antigravity, VS Code or terminal)

```bash
python -m venv venv
# Windows:  venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:8000`

## Deploy on Render

1. Push this repository to GitHub (keep `best_model.pkl` in it).
2. On [render.com](https://render.com) choose **New > Blueprint** (uses `render.yaml`), or **New > Web Service** with:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app --workers 1 --threads 4 --timeout 120`
3. Python version is pinned to `3.13.18` via `render.yaml` and `.python-version`.

## Project Structure

| File | Purpose |
|---|---|
| `app.py` | Flask routes, localized context, prediction, validation |
| `credit_summary.py` | AI Executive Credit Memo & policy recommendations |
| `ratios_radar.py` | 5-pillar radar chart geometry and financial ratios |
| `analytics_db.py` | SQLite audit log database, KPI calculations & CSV export |
| `translations.py` | Bilingual translation dictionary (English & বাংলা) |
| `best_model.pkl` | Trained scikit-learn Gradient Boosting pipeline |
| `templates/` | `base.html`, `index.html`, `result.html`, `analytics.html` |
| `static/` | Responsive CSS design system, SVG favicon, and client JS |

## JSON API

- `POST /api/predict` with the 12 fields as JSON returns risk level, confidence, class probabilities, financial ratios, and the executive credit memo.
- `GET /healthz` is the health check.
- `GET /analytics/export` downloads the audit log in CSV format.
