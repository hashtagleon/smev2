"""Database persistence and portfolio analytics for SME Risk Detector."""

import csv
import io
import json
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "sme_records.db"


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS assessments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL,
                district TEXT NOT NULL,
                location_type TEXT NOT NULL,
                sector TEXT NOT NULL,
                business_age_years INTEGER NOT NULL,
                owner_experience_years INTEGER NOT NULL,
                banking_years INTEGER NOT NULL,
                annual_revenue REAL NOT NULL,
                loan_amount REAL NOT NULL,
                debt_to_asset_ratio REAL NOT NULL,
                num_employees INTEGER NOT NULL,
                collateral_value REAL NOT NULL,
                past_defaults INTEGER NOT NULL,
                risk_level TEXT NOT NULL,
                confidence REAL NOT NULL,
                scale_position REAL NOT NULL,
                demo_title TEXT
            )
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_created_at ON assessments(created_at)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_risk_level ON assessments(risk_level)")
        
        # Check if table is empty, seed with realistic records
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM assessments")
        if cur.fetchone()[0] == 0:
            seed_initial_records(conn)


def seed_initial_records(conn):
    now = datetime.now()
    records = [
        ("Dhaka", "urban", "textiles", 8, 14, 6, 12500000, 3500000, 0.45, 35, 4200000, 0, "low", 0.88, 0.12, "Export Garments Ltd", 1),
        ("Chittagong", "urban", "trading", 12, 18, 9, 24000000, 6000000, 0.52, 18, 7500000, 0, "low", 0.91, 0.09, "Karnafuli Traders", 2),
        ("Khulna", "semi_urban", "textiles", 2, 20, 3, 5850000, 2140000, 1.21, 11, 0, 0, "high", 0.84, 0.84, "Leveraged textile unit", 3),
        ("Sylhet", "urban", "trading", 16, 2, 7, 3600000, 1690000, 0.69, 24, 510000, 0, "medium", 0.72, 0.53, "Established trading shop", 4),
        ("Khulna", "rural", "agriculture", 13, 9, 5, 6400000, 2920000, 0.58, 8, 3580000, 0, "low", 0.86, 0.14, "Secured agro business", 5),
        ("Dhaka", "urban", "services", 4, 6, 2, 4500000, 2200000, 0.85, 12, 800000, 1, "high", 0.79, 0.81, "Apex IT Solutions", 6),
        ("Bogra", "semi_urban", "agriculture", 9, 15, 6, 8200000, 2500000, 0.62, 14, 3000000, 0, "low", 0.83, 0.18, "North Bengal Agro", 7),
        ("Rajshahi", "urban", "manufacturing", 7, 12, 4, 7100000, 3100000, 0.92, 22, 1500000, 1, "high", 0.81, 0.85, "Barendra Metal Works", 8),
        ("Comilla", "semi_urban", "retail", 10, 11, 7, 5400000, 1800000, 0.55, 6, 2000000, 0, "low", 0.85, 0.16, "Moynamoti Fashion Store", 9),
        ("Gazipur", "semi_urban", "textiles", 5, 8, 3, 9800000, 4200000, 0.78, 45, 2100000, 0, "medium", 0.68, 0.58, "Symphony Knitwear", 11),
        ("Narayanganj", "urban", "manufacturing", 14, 22, 10, 18500000, 5000000, 0.48, 30, 6000000, 0, "low", 0.92, 0.08, "Shitalakhya Paper Mills", 13),
        ("Rangpur", "rural", "agriculture", 3, 5, 1, 3200000, 1800000, 1.10, 7, 400000, 2, "high", 0.89, 0.92, "Teesta Poultry Farm", 15),
        ("Jessore", "semi_urban", "trading", 8, 14, 5, 6900000, 2400000, 0.64, 9, 1800000, 0, "medium", 0.65, 0.52, "Rupali Auto Parts", 17),
        ("Dhaka", "urban", "retail", 6, 9, 4, 8800000, 3000000, 0.71, 15, 2500000, 0, "medium", 0.67, 0.49, "Gulshan Super Market Mart", 20),
        ("Sylhet", "semi_urban", "services", 11, 16, 8, 7500000, 2000000, 0.42, 16, 3200000, 0, "low", 0.90, 0.10, "Surma Diagnostic Center", 23),
        ("Mymensingh", "rural", "agriculture", 6, 10, 3, 4100000, 2100000, 0.88, 10, 900000, 1, "high", 0.78, 0.80, "Brahmaputra Fisheries", 26),
    ]
    
    cur = conn.cursor()
    for row in records:
        days_ago = row[16]
        created = (now - timedelta(days=days_ago, hours=days_ago % 12)).strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("""
            INSERT INTO assessments (
                district, location_type, sector, business_age_years, owner_experience_years,
                banking_years, annual_revenue, loan_amount, debt_to_asset_ratio, num_employees,
                collateral_value, past_defaults, risk_level, confidence, scale_position,
                demo_title, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, row[:16] + (created,))
    conn.commit()


def save_assessment(values, result, demo_title=None):
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO assessments (
                district, location_type, sector, business_age_years, owner_experience_years,
                banking_years, annual_revenue, loan_amount, debt_to_asset_ratio, num_employees,
                collateral_value, past_defaults, risk_level, confidence, scale_position,
                demo_title, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            values["district"], values["location_type"], values["sector"],
            values["business_age_years"], values["owner_experience_years"], values["banking_years"],
            values["annual_revenue"], values["loan_amount"], values["debt_to_asset_ratio"],
            values["num_employees"], values["collateral_value"], values["past_defaults"],
            result["level"], result["confidence"], result["scale_position"],
            demo_title, now_str
        ))
        conn.commit()
        return cur.lastrowid


def get_analytics_summary():
    with get_db() as conn:
        cur = conn.cursor()
        
        # Overall Totals
        cur.execute("""
            SELECT 
                COUNT(*) as total_count,
                COALESCE(AVG(loan_amount), 0) as avg_loan,
                COALESCE(SUM(loan_amount), 0) as total_loan,
                COALESCE(AVG(collateral_value / MAX(loan_amount, 1)), 0) * 100 as avg_collateral_cov,
                COALESCE(AVG(debt_to_asset_ratio), 0) as avg_dta,
                COALESCE(AVG(business_age_years), 0) as avg_age
            FROM assessments
        """)
        totals = dict(cur.fetchone())
        
        # Risk Counts
        cur.execute("SELECT risk_level, COUNT(*) as cnt FROM assessments GROUP BY risk_level")
        risk_map = {"low": 0, "medium": 0, "high": 0}
        for row in cur.fetchall():
            risk_map[row["risk_level"]] = row["cnt"]
        
        total = totals["total_count"] or 1
        risk_pcts = {
            k: round((v / total) * 100, 1) for k, v in risk_map.items()
        }
        
        # Sector Breakdown
        cur.execute("""
            SELECT 
                sector,
                COUNT(*) as total,
                SUM(CASE WHEN risk_level = 'high' THEN 1 ELSE 0 END) as high_risk_count,
                SUM(CASE WHEN risk_level = 'medium' THEN 1 ELSE 0 END) as medium_risk_count,
                SUM(CASE WHEN risk_level = 'low' THEN 1 ELSE 0 END) as low_risk_count,
                AVG(loan_amount) as avg_loan
            FROM assessments
            GROUP BY sector
            ORDER BY total DESC
        """)
        sectors = []
        for r in cur.fetchall():
            tot = r["total"]
            sectors.append({
                "sector": r["sector"],
                "total": tot,
                "high_count": r["high_risk_count"],
                "medium_count": r["medium_risk_count"],
                "low_count": r["low_risk_count"],
                "high_pct": round((r["high_risk_count"] / tot) * 100, 1) if tot else 0,
                "avg_loan": r["avg_loan"]
            })
            
        # District Spread (Top 8)
        cur.execute("""
            SELECT 
                district,
                COUNT(*) as total,
                SUM(CASE WHEN risk_level = 'high' THEN 1 ELSE 0 END) as high_risk_count
            FROM assessments
            GROUP BY district
            ORDER BY total DESC
            LIMIT 8
        """)
        districts = [dict(r) for r in cur.fetchall()]
        
        # Recent Records (last 25)
        cur.execute("""
            SELECT * FROM assessments
            ORDER BY id DESC
            LIMIT 25
        """)
        recent = [dict(r) for r in cur.fetchall()]
        
        return {
            "totals": totals,
            "risk_counts": risk_map,
            "risk_pcts": risk_pcts,
            "sectors": sectors,
            "districts": districts,
            "recent": recent
        }


def export_csv_data():
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM assessments ORDER BY id DESC")
        rows = cur.fetchall()
        
        output = io.StringIO()
        writer = csv.writer(output)
        if rows:
            writer.writerow(rows[0].keys())
            for row in rows:
                writer.writerow(list(row))
        else:
            writer.writerow(["id", "created_at", "district", "sector", "risk_level"])
        return output.getvalue()
