"""Advanced financial health ratios and 5-pillar credit radar chart generator."""

import math


def calculate_advanced_ratios(values):
    loan = float(values.get("loan_amount", 0))
    revenue = float(values.get("annual_revenue", 0))
    collateral = float(values.get("collateral_value", 0))
    dta = float(values.get("debt_to_asset_ratio", 0))
    employees = int(values.get("num_employees", 1) or 1)
    
    loan_to_revenue = (loan / revenue) if revenue > 0 else 0.0
    collateral_cover = (collateral / loan) if loan > 0 else 0.0
    ltv = ((loan / collateral) * 100) if collateral > 0 else None
    rev_per_employee = (revenue / employees) if employees > 0 else revenue
    
    # Financial Health Resilience Composite Score (0 - 100)
    # 1. DTA Component (35 pts max): lower is better
    dta_pts = max(0.0, 35.0 * (1.0 - (min(dta, 1.2) / 1.2)))
    # 2. Collateral Component (35 pts max): 1.0x cover gives full points
    col_pts = min(35.0, 35.0 * min(collateral_cover, 1.0))
    # 3. Loan-to-Revenue Burden (30 pts max): < 30% is ideal
    if loan_to_revenue <= 0.3:
        lt_pts = 30.0
    else:
        lt_pts = max(0.0, 30.0 * (1.0 - ((min(loan_to_revenue, 0.8) - 0.3) / 0.5)))
        
    health_score = int(round(dta_pts + col_pts + lt_pts))
    health_score = max(5, min(100, health_score))
    
    if health_score >= 75:
        health_tier = "robust"
    elif health_score >= 45:
        health_tier = "moderate"
    else:
        health_tier = "vulnerable"

    return {
        "loan_to_revenue": loan_to_revenue,
        "collateral_cover": collateral_cover,
        "ltv": ltv,
        "rev_per_employee": rev_per_employee,
        "debt_to_asset_ratio": dta,
        "health_score": health_score,
        "health_tier": health_tier
    }


def calculate_credit_radar(values):
    """
    Computes 5-pillar scores (0-100) and precalculates SVG coordinates
    for an embedded, sharp vector Radar Chart.
    """
    bus_age = int(values.get("business_age_years", 0))
    owner_exp = int(values.get("owner_experience_years", 0))
    dta = float(values.get("debt_to_asset_ratio", 0))
    loan = float(values.get("loan_amount", 1))
    collateral = float(values.get("collateral_value", 0))
    banking_yrs = int(values.get("banking_years", 0))
    defaults = int(values.get("past_defaults", 0))

    # 1. Stability (0-100): Business tenure + owner experience
    stability = min(100, int((min(bus_age, 15) / 15.0) * 50 + (min(owner_exp, 20) / 20.0) * 50))
    stability = max(15, stability)

    # 2. Financial Leverage (0-100): Debt to Asset management
    leverage = max(10, min(100, int((1.2 - min(dta, 1.2)) / 1.2 * 100)))

    # 3. Collateral Cover (0-100): Pledged security vs requested limit
    col_ratio = collateral / max(loan, 1.0)
    collateral_score = min(100, max(10, int(min(col_ratio, 1.25) / 1.25 * 100)))

    # 4. Banking Trust (0-100): Relationship history
    banking_score = min(100, max(15, int((min(banking_yrs, 10) / 10.0) * 100)))

    # 5. Credit Discipline (0-100): CIB past default record
    if defaults == 0:
        discipline = 100
    elif defaults == 1:
        discipline = 55
    elif defaults == 2:
        discipline = 25
    else:
        discipline = 10

    pillars = [
        {"key": "pillar_stability", "score": stability, "angle_idx": 0},
        {"key": "pillar_leverage", "score": leverage, "angle_idx": 1},
        {"key": "pillar_collateral", "score": collateral_score, "angle_idx": 2},
        {"key": "pillar_banking", "score": banking_score, "angle_idx": 3},
        {"key": "pillar_discipline", "score": discipline, "angle_idx": 4},
    ]

    # Precalculate SVG layout: center (170, 150), radius = 100
    cx, cy, r = 170.0, 150.0, 100.0
    angles = [-math.pi / 2.0 + i * (2.0 * math.pi / 5.0) for i in range(5)]

    # Grid rings for 20%, 40%, 60%, 80%, 100%
    grid_rings = []
    for level in [0.2, 0.4, 0.6, 0.8, 1.0]:
        pts = []
        for a in angles:
            x = cx + r * level * math.cos(a)
            y = cy + r * level * math.sin(a)
            pts.append(f"{x:.1f},{y:.1f}")
        grid_rings.append(" ".join(pts))

    # Axis spokes (center to 100% outer radius)
    spokes = []
    for a in angles:
        x2 = cx + r * math.cos(a)
        y2 = cy + r * math.sin(a)
        spokes.append({"x1": cx, "y1": cy, "x2": round(x2, 1), "y2": round(y2, 1)})

    # Data polygon and vertex markers
    data_pts = []
    vertex_markers = []
    for i, p in enumerate(pillars):
        a = angles[i]
        mag = (p["score"] / 100.0) * r
        x = cx + mag * math.cos(a)
        y = cy + mag * math.sin(a)
        data_pts.append(f"{x:.1f},{y:.1f}")
        
        # Label position slightly outside radius
        lx = cx + (r + 26) * math.cos(a)
        ly = cy + (r + 18) * math.sin(a)
        
        vertex_markers.append({
            "key": p["key"],
            "score": p["score"],
            "x": round(x, 1),
            "y": round(y, 1),
            "lx": round(lx, 1),
            "ly": round(ly, 1)
        })

    data_polygon_str = " ".join(data_pts)

    return {
        "pillars": pillars,
        "grid_rings": grid_rings,
        "spokes": spokes,
        "data_polygon": data_polygon_str,
        "vertices": vertex_markers,
        "overall_average": int(round(sum(p["score"] for p in pillars) / 5.0))
    }
