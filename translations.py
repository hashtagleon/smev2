"""Bilingual translations (English and Bengali) for SME Risk Detector."""

TRANSLATIONS = {
    "en": {
        "app_title": "SME Risk Detector",
        "app_tagline": "Automated SME Credit Risk Appraisal Platform",
        "step_1": "Step 1 of 2: applicant details",
        "step_2": "Step 2 of 2: result",
        "rail_form_title": "Check an SME loan applicant",
        "rail_form_lead": "Enter the business profile, financials and credit history. The model returns a risk level and how sure it is.",
        "sample_header": "Try a sample applicant",
        "check_fields_alert": "Check highlighted fields before predicting.",
        
        # Sections
        "sec_business": "Business profile",
        "sec_business_desc": "Where the business operates, and how long it and its owner have been at it.",
        "sec_financials": "Financials",
        "sec_financials_desc": "Amounts are in Bangladeshi taka (BDT).",
        "sec_security": "Credit history",
        "sec_security_desc": "Serious delinquencies and write-offs on record.",
        
        # Fields
        "field_district": "District",
        "field_district_hint": "Each district carries its own baseline risk.",
        "field_location_type": "Location type",
        "field_location_type_hint": "Urban areas tend to lower the risk slightly.",
        "field_sector": "Sector",
        "field_sector_hint": "Some sectors run riskier than others.",
        "field_business_age": "Business age",
        "field_business_age_hint": "Years the business has operated.",
        "field_owner_exp": "Owner experience",
        "field_owner_exp_hint": "Years of experience of the main owner or manager.",
        "field_banking_years": "Banking relationship",
        "field_banking_years_hint": "Years with their main bank.",
        "field_annual_rev": "Annual revenue",
        "field_annual_rev_hint": "Total yearly sales in BDT.",
        "field_loan_amount": "Loan amount",
        "field_loan_amount_hint": "Requested or outstanding loan in BDT.",
        "field_debt_asset": "Debt-to-asset ratio",
        "field_debt_asset_hint": "Total debt divided by total assets, from 0 to 2.",
        "field_employees": "Employees",
        "field_employees_hint": "Full-time staff.",
        "field_collateral": "Collateral value",
        "field_collateral_hint": "Realizable value pledged against this loan in BDT.",
        "field_defaults": "Past defaults",
        "field_defaults_hint": "Number of defaults or write-offs.",
        
        # Actions
        "btn_predict": "Predict risk",
        "btn_clear": "Clear form",
        "btn_edit": "Edit this entry",
        "btn_new": "Assess another applicant",
        "choose_one": "Choose one",
        "demo_result": "View demo result",
        "form_footer_note": "The next page shows the risk level, class probabilities and confidence.",
        "result_footer_note": "This is a model estimate to support a credit officer's review. It is not a lending decision.",
        
        # Results
        "verdict_high": "High Risk",
        "verdict_medium": "Medium Risk",
        "verdict_low": "Low Risk",
        "confidence_lead": "The model is {pct} sure of this call.",
        "confidence_close": "That is a modest margin, so treat it as a close case.",
        "confidence_clear": "That is a clear margin over the other two levels.",
        
        "risk_scale_title": "Where this applicant sits",
        "risk_scale_desc": "The needle is weighted by all three probabilities, so a split result lands between zones.",
        
        "class_probs_title": "Class probabilities",
        "class_probs_desc": "How the model splits its belief across the three levels.",
        
        "ratios_title": "Loan against the business",
        "ratios_desc": "Two ratios worked out from the entries below.",
        "ratio_loan_size": "Loan size",
        "ratio_loan_size_sub": "of annual revenue",
        "ratio_collateral": "Collateral cover",
        "ratio_collateral_sub": "of the loan amount",
        
        "entered_values_title": "What was entered",
        "entered_values_desc": "The exact values the model scored.",
        "years_unit": "yr"
    },
    
    "bn": {
        "app_title": "এসএমই ঝুঁকি নিরূপণ",
        "app_tagline": "স্বয়ংক্রিয় এসএমই ঋণ ঝুঁকি মূল্যায়ন প্ল্যাটফর্ম",
        "step_1": "ধাপ ১/২: আবেদনকারীর বিবরণ",
        "step_2": "ধাপ ২/২: ফলাফল",
        "rail_form_title": "এসএমই ঋণ আবেদন যাচাই",
        "rail_form_lead": "ব্যবসার তথ্য, আর্থিক বিবরণী ও ক্রেডিট হিস্ট্রি প্রদান করুন। মডেলটি ঝুঁকি স্তর এবং নির্ভুলতা প্রদর্শন করবে।",
        "sample_header": "নমুনা আবেদনকারী দেখুন",
        "check_fields_alert": "মূল্যায়ন করার আগে চিহ্নিত ফিল্ডগুলো সংশোধন করুন।",
        
        # Sections
        "sec_business": "ব্যবসার বিবরণ",
        "sec_business_desc": "ব্যবসার অবস্থান এবং উদ্যোক্তা কতদিন ধরে ব্যবসা পরিচালনা করছেন।",
        "sec_financials": "আর্থিক বিবরণী",
        "sec_financials_desc": "অর্থের পরিমাণ বাংলাদেশি টাকায় (BDT)।",
        "sec_security": "ক্রেডিট হিস্ট্রি",
        "sec_security_desc": "বিগত ঋণ খেলাপি বা বিলম্বের রেকর্ড।",
        
        # Fields
        "field_district": "জেলা",
        "field_district_hint": "প্রতিটি জেলার নিজস্ব অর্থনৈতিক ঝুঁকি সূচক রয়েছে।",
        "field_location_type": "এলাকার ধরন",
        "field_location_type_hint": "শহরাঞ্চলে সাধারণত ব্যবসায়িক ঝুঁকি কিছুটা কম থাকে।",
        "field_sector": "খাত বা শিল্প",
        "field_sector_hint": "কিছু খাতে অন্য খাতের চেয়ে ঝুঁকি তুলনামূলক বেশি থাকে।",
        "field_business_age": "ব্যবসার বয়স",
        "field_business_age_hint": "প্রতিষ্ঠানটি কত বছর ধরে পরিচালিত হচ্ছে।",
        "field_owner_exp": "উদ্যোক্তার অভিজ্ঞতা",
        "field_owner_exp_hint": "প্রধান মালিক বা ব্যবস্থাপকের কাজের অভিজ্ঞতা (বছর)।",
        "field_banking_years": "ব্যাংকিং সম্পর্ক",
        "field_banking_years_hint": "প্রধান ব্যাংকের সাথে লেনদেনের সময়কাল (বছর)।",
        "field_annual_rev": "বার্ষিক আয়",
        "field_annual_rev_hint": "মোট বাৎসরিক আয় (টাকায়)।",
        "field_loan_amount": "ঋণের পরিমাণ",
        "field_loan_amount_hint": "প্রার্থিত ঋণের পরিমাণ (টাকায়)।",
        "field_debt_asset": "ঋণ ও সম্পদের অনুপাত",
        "field_debt_asset_hint": "মোট দায়ের বিপরীতে মোট সম্পদের অনুপাত (০ থেকে ২)।",
        "field_employees": "কর্মীর সংখ্যা",
        "field_employees_hint": "প্রতিষ্ঠানে কর্মরত নিয়মিত কর্মী।",
        "field_collateral": "জামানতের মূল্য",
        "field_collateral_hint": "ঋণের বিপরীতে বন্ধকীকৃত সম্পদের মূল্য (টাকায়)।",
        "field_defaults": "পূর্ববর্তী ঋণ খেলাপি",
        "field_defaults_hint": "পূর্বে ঋণ খেলাপির সংখ্যা।",
        
        # Actions
        "btn_predict": "ঝুঁকি যাচাই করুন",
        "btn_clear": "রিসেট করুন",
        "btn_edit": "তথ্য পরিবর্তন করুন",
        "btn_new": "আরেকটি আবেদন যাচাই করুন",
        "choose_one": "নির্বাচন করুন",
        "demo_result": "নমুনা ফলাফল দেখুন",
        "form_footer_note": "পরবর্তী পাতায় ঝুঁকির মাত্রা, ক্লাস সম্ভাবনা ও কনফিডেন্স প্রদর্শিত হবে।",
        "result_footer_note": "এটি লোন অফিসারদের সহায়তার জন্য মডেলের অনুমান। এটি চূড়ান্ত ঋণ অনুমোদন সিদ্ধান্ত নয়।",
        
        # Results
        "verdict_high": "উচ্চ ঝুঁকি",
        "verdict_medium": "মাঝারি ঝুঁকি",
        "verdict_low": "নিম্ন ঝুঁকি",
        "confidence_lead": "মডেলটি {pct} নিশ্চিতভাবে এই মূল্যায়ন করেছে।",
        "confidence_close": "পার্থক্য খুব সামান্য, তাই এটিকে সতর্কতার সাথে বিবেচনা করুন।",
        "confidence_clear": "অন্য দুটি স্তরের তুলনায় এটি সুস্পষ্ট ব্যবধানে নির্ধারিত।",
        
        "risk_scale_title": "ঝুঁকি স্কেল অবস্থান",
        "risk_scale_desc": "তিনটি সম্ভাব্যতার ভিত্তিতে কাঁটার অবস্থান নির্ধারিত হয়েছে।",
        
        "class_probs_title": "সম্ভাবনা বিন্যাস",
        "class_probs_desc": "মডেলটি তিনটি ঝুঁকি স্তরের মধ্যে সম্ভাবনা যেভাবে ভাগ করেছে।",
        
        "ratios_title": "ব্যবসায়ের বিপরীতে ঋণের অনুপাত",
        "ratios_desc": "প্রদত্ত তথ্যের ভিত্তিতে দুটি প্রধান অনুপাত।",
        "ratio_loan_size": "ঋণের আকার",
        "ratio_loan_size_sub": "বার্ষিক আয়ের",
        "ratio_collateral": "জামানত কভারেজ",
        "ratio_collateral_sub": "মোট ঋণের পরিমাণের",
        
        "entered_values_title": "আবেদনকারীর তথ্যাবলী",
        "entered_values_desc": "মডেলে মূল্যায়নের জন্য জমাকৃত সঠিক মানসমূহ।",
        "years_unit": "বছর"
    }
}

SECTOR_MAP = {
    "agriculture": {"en": "Agriculture", "bn": "কৃষি খাত"},
    "manufacturing": {"en": "Manufacturing", "bn": "উৎপাদন শিল্প"},
    "retail": {"en": "Retail", "bn": "খুচরা ব্যবসা"},
    "services": {"en": "Services", "bn": "সেবা খাত"},
    "textiles": {"en": "Textiles", "bn": "পোশাক ও টেক্সটাইল"},
    "trading": {"en": "Trading", "bn": "ট্রেডিং ও পাইকারি ব্যবসা"},
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
