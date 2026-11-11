"""Bilingual translations (English and Bengali) for SME Risk Detector."""

TRANSLATIONS = {
    "en": {
        "app_title": "SME Risk Detector",
        "app_tagline": "Automated SME Credit Risk Appraisal Platform",
        "nav_assess": "Assessment Form",
        "nav_analytics": "Portfolio Analytics",
        "step_1": "Step 1 of 2: applicant details",
        "step_2": "Step 2 of 2: risk assessment & credit memo",
        "rail_form_title": "Check an SME loan applicant",
        "rail_form_lead": "Enter the business profile, financials and credit history. The model returns a calibrated risk level, key ratios, and credit committee recommendations.",
        "sample_header": "Try a sample applicant",
        "check_fields_alert": "Check highlighted fields before predicting.",
        
        # Sections
        "sec_business": "Business profile",
        "sec_business_desc": "Where the business operates, and how long it and its owner have been in business.",
        "sec_financials": "Financials",
        "sec_financials_desc": "Annual revenue, the requested loan and total debt compared to assets.",
        "sec_security": "Security and credit history",
        "sec_security_desc": "Pledged collateral, team size and record of past loan defaults.",
        
        # Fields
        "field_district": "District",
        "field_district_hint": "Regional economic baseline risk across Bangladesh.",
        "field_location_type": "Location type",
        "field_location_type_hint": "Urban and semi-urban clusters often reflect higher market liquidity.",
        "field_sector": "Sector",
        "field_sector_hint": "Industry sector risk variance.",
        "field_business_age": "Business age",
        "field_business_age_hint": "Years the enterprise has been actively operating.",
        "field_owner_exp": "Owner experience",
        "field_owner_exp_hint": "Years of commercial experience of primary promoter/manager.",
        "field_banking_years": "Banking relationship",
        "field_banking_years_hint": "Tenure of active relationship with formal banking sector.",
        "field_annual_rev": "Annual revenue",
        "field_annual_rev_hint": "Total verifiable gross annual revenue in BDT.",
        "field_loan_amount": "Loan amount",
        "field_loan_amount_hint": "Requested credit limit / loan principal in BDT.",
        "field_debt_asset": "Debt-to-asset ratio",
        "field_debt_asset_hint": "Total liabilities divided by total tangible assets (0.00 to 2.00).",
        "field_employees": "Employees",
        "field_employees_hint": "Full-time equivalent workforce size.",
        "field_collateral": "Collateral value",
        "field_collateral_hint": "Estimated forced-sale value of pledged assets in BDT.",
        "field_defaults": "Past defaults",
        "field_defaults_hint": "Number of previous credit defaults or restructured facilities.",
        
        # Actions
        "btn_predict": "Assess Loan Risk",
        "btn_clear": "Reset Form",
        "btn_edit": "Edit Applicant Data",
        "btn_new": "New Assessment",
        "btn_export_csv": "Export CSV Audit Log",
        "btn_back_form": "Back to Form",
        "choose_one": "Choose one",
        
        # Results
        "verdict_high": "High Risk",
        "verdict_medium": "Medium Risk",
        "verdict_low": "Low Risk",
        "confidence_lead": "The gradient boosting model is {pct} confident in this risk rating.",
        "confidence_close": "This is a close borderline case; secondary committee review recommended.",
        "confidence_clear": "Decisive margin over the other risk tiers.",
        "risk_scale_title": "Risk Scale Position",
        "risk_scale_desc": "Continuous spectrum needle derived from probability weighting across Low, Medium, and High.",
        "class_probs_title": "Class Probabilities",
        "class_probs_desc": "Machine learning model's calibrated probability distribution.",
        "advanced_ratios_title": "Key Financial & Solvency Metrics",
        "advanced_ratios_desc": "Core credit ratios benchmarked against SME lending standards.",
        "radar_title": "Credit Profile 5-Pillar Radar",
        "radar_desc": "Multidimensional strength mapping across stability, leverage, collateral, banking relationship, and credit history.",
        "ai_memo_title": "AI Executive Credit Memo & Insights",
        "ai_memo_desc": "Automated credit risk synthesis and underwriting policy recommendations.",
        "strengths_title": "Key Positive Signals",
        "risks_title": "Credit Risk Alerts",
        "recommendation_title": "Underwriter Recommendation",
        "entered_values_title": "Application Data Summary",
        "entered_values_desc": "Complete verified inputs submitted for scoring.",
        
        # Metrics
        "metric_loan_rev": "Loan-to-Revenue",
        "metric_collateral_cov": "Collateral Coverage",
        "metric_ltv": "Loan-to-Value (LTV)",
        "metric_rev_per_emp": "Revenue per Employee",
        "metric_dta": "Debt-to-Asset",
        "metric_resilience": "Financial Health Score",
        
        # Pillars
        "pillar_stability": "Stability",
        "pillar_leverage": "Financial Leverage",
        "pillar_collateral": "Collateral Cover",
        "pillar_banking": "Banking Trust",
        "pillar_discipline": "Credit Discipline",
        
        # Analytics
        "analytics_title": "Portfolio Risk Analytics",
        "analytics_subtitle": "Real-time audit log, risk distributions, and SME credit trends.",
        "kpi_total": "Total Assessed",
        "kpi_avg_loan": "Average Loan Size",
        "kpi_avg_collateral": "Avg. Collateral Cover",
        "kpi_high_risk_share": "High Risk Share",
        "portfolio_breakdown": "Portfolio Risk Breakdown",
        "sector_breakdown": "Sector Distribution & Risk Exposure",
        "district_breakdown": "District Geographic Spread",
        "audit_log_title": "Recent Assessment Audit Log",
        "col_date": "Timestamp",
        "col_applicant": "Sector / District",
        "col_loan": "Loan Request",
        "col_collateral": "Collateral",
        "col_verdict": "Risk Rating",
        "col_confidence": "Confidence",
        "col_action": "Action",
        "view_details": "Inspect",
        "empty_log": "No assessments recorded yet."
    },
    
    "bn": {
        "app_title": "এসএমই ঝুঁকি নিরূপণ",
        "app_tagline": "স্বয়ংক্রিয় এসএমই ঋণ ঝুঁকি মূল্যায়ন প্ল্যাটফর্ম",
        "nav_assess": "মূল্যায়ন ফরম",
        "nav_analytics": "পোর্টফোলিও অ্যানালিটিক্স",
        "step_1": "ধাপ ১/২: আবেদনকারীর বিবরণ",
        "step_2": "ধাপ ২/২: ঝুঁকি মূল্যায়ন ও ক্রেডিট মেমো",
        "rail_form_title": "এসএমই ঋণ আবেদন যাচাই",
        "rail_form_lead": "ব্যবসার তথ্য, আর্থিক বিবরণী ও ক্রেডিট হিস্ট্রি প্রদান করুন। মেশিন লার্নিং মডেল নির্ভুল ঝুঁকি স্তর, ফাইন্যান্সিয়াল রেশিও এবং ক্রেডিট কমিটির সুপারিশ প্রদান করবে।",
        "sample_header": "নমুনা আবেদনকারী দেখুন",
        "check_fields_alert": "মূল্যায়ন করার আগে চিহ্নিত ফিল্ডগুলো সংশোধন করুন।",
        
        # Sections
        "sec_business": "ব্যবসার সাধারণ পরিচিতি",
        "sec_business_desc": "ব্যবসার অবস্থান এবং উদ্যোক্তার সামগ্রিক অভিজ্ঞতা।",
        "sec_financials": "আর্থিক সক্ষমতা",
        "sec_financials_desc": "বার্ষিক আয়, কাঙ্ক্ষিত ঋণের পরিমাণ এবং সম্পদের বিপরীতে ঋণের অনুপাত।",
        "sec_security": "জামানত ও পূর্ববর্তী ঋণ পরিশোধ",
        "sec_security_desc": "বন্ধকীকৃত জামানত, মোট জনবল এবং অতীত খেলাপি রেকর্ড।",
        
        # Fields
        "field_district": "জেলা",
        "field_district_hint": "বাংলাদেশ ব্যাংকের জেলাভিত্তিক আর্থিক ঝুঁকি সূচক।",
        "field_location_type": "এলাকার ধরন",
        "field_location_type_hint": "শহুরে ও আধা-শহুরে এলাকায় বাজার তারল্য সাধারণত বেশি থাকে।",
        "field_sector": "খাত বা শিল্প",
        "field_sector_hint": "শিল্প খাতভেদে ব্যবসায়িক ঝুঁকির ভিন্নতা থাকে।",
        "field_business_age": "ব্যবসার বয়স",
        "field_business_age_hint": "প্রতিষ্ঠানটি সক্রিয়ভাবে কত বছর ধরে পরিচালিত হচ্ছে।",
        "field_owner_exp": "উদ্যোক্তার অভিজ্ঞতা",
        "field_owner_exp_hint": "প্রধান স্বত্বাধিকারী বা পরিচালকের বাণিজ্যিক অভিজ্ঞতা (বছর)।",
        "field_banking_years": "ব্যাংকিং সম্পর্ক",
        "field_banking_years_hint": "আনুষ্ঠানিক ব্যাংকিং চ্যানেলে লেনদেনের বয়স (বছর)।",
        "field_annual_rev": "বার্ষিক আয় (টার্নওভার)",
        "field_annual_rev_hint": "যাচাইকৃত মোট বাৎসরিক গ্রস রাজস্ব (টাকায়)।",
        "field_loan_amount": "ঋণের পরিমাণ",
        "field_loan_amount_hint": "প্রার্থিত ঋণের মূল পরিমাণ (টাকায়)।",
        "field_debt_asset": "ঋণ ও সম্পদের অনুপাত",
        "field_debt_asset_hint": "মোট দায়ের বিপরীতে মোট দৃশ্যমান সম্পদের অনুপাত (০.০০ থেকে ২.০০)।",
        "field_employees": "কর্মীর সংখ্যা",
        "field_employees_hint": "প্রতিষ্ঠানটিতে কর্মরত মোট নিয়মিত জনবল।",
        "field_collateral": "জামানতের মূল্য",
        "field_collateral_hint": "বন্ধকীকৃত স্থাবর/অস্থাবর সম্পত্তির আনুমানিক নিলাম মূল্য (টাকায়)।",
        "field_defaults": "পূর্ববর্তী ঋণ খেলাপি",
        "field_defaults_hint": "বিগত দিনে ঋণ খেলাপি বা পুনর্গঠন (CIB রেকর্ড)।",
        
        # Actions
        "btn_predict": "ঋণ ঝুঁকি নিরূপণ করুন",
        "btn_clear": "রিসেট করুন",
        "btn_edit": "তথ্য পরিবর্তন করুন",
        "btn_new": "নতুন মূল্যায়ন",
        "btn_export_csv": "CSV অডিট লগ ডাউনলোড",
        "btn_back_form": "ফরমে ফিরে যান",
        "choose_one": "নির্বাচন করুন",
        
        # Results
        "verdict_high": "উচ্চ ঝুঁকি",
        "verdict_medium": "মাঝারি ঝুঁকি",
        "verdict_low": "নিম্ন ঝুঁকি",
        "confidence_lead": "মডেলটি {pct} আত্মবিশ্বাসের সাথে এই ঝুঁকি নির্ধারণ করেছে।",
        "confidence_close": "এটি একটি প্রান্তিক কেস; ক্রেডিট কমিটির বিশেষ পুঙ্খানুপুঙ্খ পর্যালোচনা আবশ্যক।",
        "confidence_clear": "অন্যান্য ঝুঁকি স্তরের চেয়ে স্পষ্ট ব্যবধানে নির্ধারিত।",
        "risk_scale_title": "রিস্ক স্কেল অবস্থান",
        "risk_scale_desc": "নিম্ন, মাঝারি এবং উচ্চ সম্ভাবনার ভারযুক্ত ধারাবাহিক ঝুঁকি নির্দেশক কাঁটা।",
        "class_probs_title": "সম্ভাবনা বিন্যাস (Class Probabilities)",
        "class_probs_desc": "মেশিন লার্নিং মডেলের নিখুঁত সম্ভাবনা বণ্টন।",
        "advanced_ratios_title": "মূল আর্থিক ও ঋণ সক্ষমতা সূচক",
        "advanced_ratios_desc": "এসএমই ঋণ নীতিমালা অনুযায়ী পরীক্ষিত অত্যাবশ্যক আর্থিক অনুপাত।",
        "radar_title": "ক্রেডিট প্রোফাইল ৫-স্তম্ভ রেডার চার্ট",
        "radar_desc": "স্থায়িত্ব, সক্ষমতা, জামানত, ব্যাংকিং আস্থা ও ঋণ শৃঙ্খলার বহুমাত্রিক বিশ্লেষণ।",
        "ai_memo_title": "AI এক্সিকিউটিভ ক্রেডিট মেমো ও বিশ্লেষণ",
        "ai_memo_desc": "স্বয়ংক্রিয় ক্রেডিট ঝুঁকি সারাংশ এবং ঋণ মঞ্জুরির প্রাতিষ্ঠানিক সুপারিশ।",
        "strengths_title": "ইতিবাচক শক্তিমত্তা",
        "risks_title": "প্রধান সতর্কবার্তা ও ঝুঁকি",
        "recommendation_title": "ক্রেডিট আন্ডাররাইটারের সুপারিশ",
        "entered_values_title": "আবেদনকারীর তথ্যাবলী",
        "entered_values_desc": "মডেলে মূল্যায়নের জন্য জমাকৃত যাচাইকৃত তথ্য।",
        
        # Metrics
        "metric_loan_rev": "লোন ও বার্ষিক আয় অনুপাত",
        "metric_collateral_cov": "জামানত কভারেজ",
        "metric_ltv": "লোন-টু-ভ্যালু (LTV)",
        "metric_rev_per_emp": "কর্মী প্রতি উৎপাদনশীলতা",
        "metric_dta": "ঋণ-সম্পদ অনুপাত (DTA)",
        "metric_resilience": "আর্থিক দৃঢ়তা স্কোর",
        
        # Pillars
        "pillar_stability": "ব্যবসায়িক স্থায়িত্ব",
        "pillar_leverage": "আর্থিক সক্ষমতা",
        "pillar_collateral": "জামানত সুরক্ষা",
        "pillar_banking": "ব্যাংকিং আস্থা",
        "pillar_discipline": "ঋণ শৃঙ্খলা",
        
        # Analytics
        "analytics_title": "পোর্টফোলিও রিস্ক অ্যানালিটিক্স",
        "analytics_subtitle": "রিয়েল-টাইম অডিট লগ, ঝুঁকি বণ্টন এবং সামগ্রিক ঋণ প্রবণতা।",
        "kpi_total": "মোট মূল্যায়িত আবেদন",
        "kpi_avg_loan": "গড় ঋণের আকার",
        "kpi_avg_collateral": "গড় জামানত কভারেজ",
        "kpi_high_risk_share": "উচ্চ ঝুঁকির হার",
        "portfolio_breakdown": "পোর্টফোলিও ঝুঁকি বিভাজন",
        "sector_breakdown": "খাতভিত্তিক ঝুঁকি ও বিতরণ",
        "district_breakdown": "জেলা ভিত্তিক ভৌগোলিক বিস্তার",
        "audit_log_title": "সাম্প্রতিক মূল্যায়ন অডিট লগ",
        "col_date": "তারিখ ও সময়",
        "col_applicant": "খাত / জেলা",
        "col_loan": "ঋণের আবেদন",
        "col_collateral": "জামানত",
        "col_verdict": "ঝুঁকি স্তর",
        "col_confidence": "নির্ভরযোগ্যতা",
        "col_action": "অ্যাকশন",
        "view_details": "বিবরণ",
        "empty_log": "এখনও কোনো মূল্যায়ন রেকর্ড করা হয়নি।"
    }
}

SECTOR_MAP = {
    "agriculture": {"en": "Agriculture", "bn": "কৃষি খাত"},
    "manufacturing": {"en": "Manufacturing", "bn": "উৎপাদন শিল্প"},
    "retail": {"en": "Retail", "bn": "খুচরা ব্যবসা"},
    "services": {"en": "Services", "bn": "সেবা খাত"},
    "textiles": {"en": "Textiles & RMG", "bn": "পোশাক ও টেক্সটাইল"},
    "trading": {"en": "Wholesale & Trading", "bn": "পাইকারি ও ট্রেডিং"},
}

LOCATION_MAP = {
    "urban": {"en": "Urban", "bn": "শহুরে"},
    "semi_urban": {"en": "Semi-urban", "bn": "আধা-শহুরে"},
    "rural": {"en": "Rural", "bn": "গ্রামীণ"},
}

DISTRICT_MAP = {
    "Bagerhat": "বাগেরহাট", "Bandarban": "বান্দরবান", "Barguna": "বরগুনা", "Barisal": "বরিশাল",
    "Bhola": "ভোলা", "Bogra": "বগুড়া", "Brahmanbaria": "ব্রাহ্মণবাড়িয়া", "Chandpur": "চাঁদপুর",
    "Chapai Nawabganj": "চাঁপাইনবাবগঞ্জ", "Chattogram": "চট্টগ্রাম", "Chittagong": "চট্টগ্রাম",
    "Chuadanga": "চুয়াডাঙ্গা", "Comilla": "কুমিল্লা", "Cox's Bazar": "কক্সবাজার", "Dhaka": "ঢাকা",
    "Dinajpur": "দিনাজপুর", "Faridpur": "ফরিদপুর", "Feni": "ফেনী", "Gaibandha": "গাইবান্ধা",
    "Gazipur": "গাজীপুর", "Gopalganj": "গোপালগঞ্জ", "Habiganj": "হবিগঞ্জ", "Jamalpur": "জামালপুর",
    "Jessore": "যশোর", "Jhalokati": "ঝালকাঠি", "Jhenaidah": "ঝিনাইদহ", "Joypurhat": "জয়পুরহাট",
    "Khagrachhari": "খাগড়াছড়ি", "Khulna": "খুলনা", "Kishoreganj": "কিশোরগঞ্জ", "Kurigram": "কুড়িগ্রাম",
    "Kushtia": "কুষ্টিয়া", "Lakshmipur": "লক্ষ্মীপুর", "Lalmonirhat": "লালমনিরহাট", "Madaripur": "মাদারীপুর",
    "Magura": "মাগুরা", "Manikganj": "মানিকগঞ্জ", "Meherpur": "মেহেরপুর", "Moulvibazar": "মৌলভীবাজার",
    "Munshiganj": "মুন্সীগঞ্জ", "Mymensingh": "ময়মনসিংহ", "Naogaon": "নওগাঁ", "Narail": "নড়াইল",
    "Narayanganj": "নারায়ণগঞ্জ", "Narsingdi": "নরসিংদী", "Natore": "নাটোর", "Netrokona": "নেত্রকোনা",
    "Nilphamari": "নীলফামারী", "Noakhali": "নোয়াখালী", "Pabna": "পাবনা", "Panchagarh": "পঞ্চগড়",
    "Patuakhali": "পটুয়াখালী", "Pirojpur": "পিরোজপুর", "Rajbari": "রাজবাড়ী", "Rajshahi": "রাজশাহী",
    "Rangamati": "রাঙ্গামাটি", "Rangpur": "রংপুর", "Satkhira": "সাতক্ষীরা", "Shariatpur": "শরীয়তপুর",
    "Sherpur": "শেরপুর", "Sirajganj": "সিরাজগঞ্জ", "Sunamganj": "সুনামগঞ্জ", "Sylhet": "সিলেট",
    "Tangail": "টাঙ্গাইল", "Thakurgaon": "ঠাকুরগাঁও"
}

def localize(key, lang="en", **kwargs):
    bundle = TRANSLATIONS.get(lang, TRANSLATIONS["en"])
    text = bundle.get(key, TRANSLATIONS["en"].get(key, key))
    if kwargs:
        try:
            return text.format(**kwargs)
        except Exception:
            return text
    return text

def localize_value(val, col, lang="en"):
    if not val:
        return ""
    val_str = str(val).lower()
    if col == "sector" and val_str in SECTOR_MAP:
        return SECTOR_MAP[val_str].get(lang, val_str.capitalize())
    if col == "location_type" and val_str in LOCATION_MAP:
        return LOCATION_MAP[val_str].get(lang, val_str.capitalize())
    if col == "district":
        if lang == "bn" and str(val) in DISTRICT_MAP:
            return DISTRICT_MAP[str(val)]
        return str(val)
    if col == "risk_level":
        return localize(f"verdict_{val_str}", lang)
    return str(val)
