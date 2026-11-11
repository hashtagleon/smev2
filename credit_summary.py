"""AI-powered Executive Credit Memo & Risk Narrative Synthesizer.

Provides human-readable, institutional-grade credit appraisals and policy
recommendations in English and Bengali.
"""

from translations import localize_value


def generate_credit_summary(values, result, ratios, lang="en"):
    level = result["level"]
    confidence = result["confidence"]
    conf_pct = f"{confidence * 100:.1f}%"
    
    district = localize_value(values.get("district"), "district", lang)
    sector = localize_value(values.get("sector"), "sector", lang)
    loan = float(values.get("loan_amount", 0))
    revenue = float(values.get("annual_revenue", 0))
    collateral = float(values.get("collateral_value", 0))
    dta = float(values.get("debt_to_asset_ratio", 0))
    defaults = int(values.get("past_defaults", 0))
    bus_age = int(values.get("business_age_years", 0))
    bank_years = int(values.get("banking_years", 0))
    
    col_cover = ratios["collateral_cover"]
    lt_rev = ratios["loan_to_revenue"]
    
    strengths = []
    risks = []
    
    # Analyze Positives
    if defaults == 0:
        if lang == "bn":
            strengths.append("উত্তম ঋণ শৃঙ্খলা: অতীতে কোনো ঋণ খেলাপির রেকর্ড (CIB Clean) নেই।")
        else:
            strengths.append("Clean credit history: Zero past default record.")
            
    if col_cover >= 1.0:
        if lang == "bn":
            strengths.append(f"দৃঢ় জামানত সুরক্ষা: ঋণের বিপরীতে {col_cover*100:.0f}% মূল্যের সম্পদ বন্ধক দেওয়া হয়েছে।")
        else:
            strengths.append(f"Robust collateral backing: {col_cover*100:.0f}% coverage of loan value.")
    elif col_cover >= 0.7:
        if lang == "bn":
            strengths.append(f"সন্তোষজনক জামানত: ঋণের প্রায় {col_cover*100:.0f}% অংশ স্থাবর সম্পদে আচ্ছাদিত।")
        else:
            strengths.append(f"Moderate collateral support ({col_cover*100:.0f}% coverage).")
            
    if dta <= 0.5:
        if lang == "bn":
            strengths.append(f"সুস্থ ব্যালেন্স শিট: ঋণ ও সম্পদ অনুপাত মাত্র {dta:.2f}, যা ঝুঁকি সহনশীল।")
        else:
            strengths.append(f"Conservative financial leverage (Debt-to-Asset ratio at {dta:.2f}).")
            
    if bus_age >= 7:
        if lang == "bn":
            strengths.append(f"প্রতিষ্ঠিত ব্যবসা: প্রতিষ্ঠানটি দীর্ঘ {bus_age} বছর যাবৎ বাজারে সফলভাবে বিদ্যমান।")
        else:
            strengths.append(f"Established market presence ({bus_age} years of continuous operation).")
            
    if bank_years >= 5:
        if lang == "bn":
            strengths.append(f"দীর্ঘমেয়াদী ব্যাংকিং সম্পর্ক: {bank_years} বছরের নিয়মিত ব্যাংক লেনদেনের ইতিহাস।")
        else:
            strengths.append(f"Deep banking relationship ({bank_years} years of institutional banking history).")

    # Analyze Risk Flags
    if defaults > 0:
        if lang == "bn":
            risks.append(f"গুরুতর ঝুঁকি: আবেদনকারীর অতীতে {defaults}টি ঋণ খেলাপির দৃষ্টান্ত রয়েছে।")
        else:
            risks.append(f"Critical credit risk: Applicant has {defaults} past default incidents on record.")
            
    if col_cover < 0.4:
        if lang == "bn":
            risks.append("অপর্যাপ্ত জামানত: ঋণের সিংহভাগই অরক্ষিত (Unsecured Exposure বেশি)।")
        else:
            risks.append("Inadequate pledged collateral: High proportion of unsecured exposure.")
            
    if dta >= 0.8:
        if lang == "bn":
            risks.append(f"অতিরিক্ত দায়ভার: ঋণ ও সম্পদের অনুপাত {dta:.2f}, যা পরিশোধে চাপ সৃষ্টি করতে পারে।")
        else:
            risks.append(f"Elevated debt burden: Debt-to-Asset ratio at {dta:.2f} indicates high financial strain.")
            
    if lt_rev > 0.5:
        if lang == "bn":
            risks.append(f"উচ্চ ঋণ নির্ভরতা: ঋণের অঙ্ক বার্ষিক আয়ের {lt_rev*100:.0f}%, যা পরিশোধ সক্ষমতার ঝুঁকিতে ফেলতে পারে।")
        else:
            risks.append(f"Heavy debt burden: Requested loan equals {lt_rev*100:.0f}% of annual gross turnover.")
            
    if bus_age < 3:
        if lang == "bn":
            risks.append("নতুন উদ্যোগ: ব্যবসার বয়স ৩ বছরের কম হওয়ায় দীর্ঘমেয়াদী স্থায়িত্ব পর্যবেক্ষণাধীন।")
        else:
            risks.append("Early-stage enterprise: Limited track record (< 3 operational years).")

    # Ensure at least 1-2 items exist in both
    if not strengths:
        if lang == "bn":
            strengths.append(f"{sector} খাতে আঞ্চলিক চাহিদা ও স্বাভাবিক নগদ প্রবাহের সম্ভাবনা রয়েছে।")
        else:
            strengths.append(f"Ongoing operational cash flows observed in the {sector} sector.")
            
    if not risks:
        if lang == "bn":
            risks.append("সামষ্টিক অর্থনৈতিক মুদ্রাস্ফীতি ও বাজার চক্রজনিত স্বাভাবিক ব্যবসায়িক ঝুঁকি।")
        else:
            risks.append("Standard market cyclicality and sector-wide macroeconomic volatility.")

    # Narrative Synthesis & Committee Recommendation
    if level == "low":
        if lang == "bn":
            narrative = (
                f"আবেদনকারী প্রতিষ্ঠানটি {district} জেলায় {sector} খাতে অত্যন্ত সুদৃঢ় অবস্থানে রয়েছে। "
                f"মেশিন লার্নিং মডেল {conf_pct} আত্মবিশ্বাসের সাথে আবেদনটিকে 'নিম্ন ঝুঁকি' হিসেবে চিহ্নিত করেছে। "
                f"উদ্যোক্তার সন্তোষজনক মূলধন অনুপাত ও পরিষ্কার অতীত ঋণ পরিশোধের রেকর্ড প্রতিষ্ঠানের নগদ প্রবাহের সুরক্ষা নিশ্চিত করে।"
            )
            recommendation = (
                "ঋণ প্রস্তাবটি স্ট্যান্ডার্ড প্রাইসিং পলিসিতে অনুমোদনের জন্য উপযুক্ত। "
                "প্রস্তাবিত মেয়াদে স্বাভাবিক ত্রৈমাসিক ঋণ পর্যবেক্ষণ এবং বার্ষিক অডিট রিপোর্ট জমার শর্তে ঋণ মঞ্জুরি দেওয়া যেতে পারে।"
            )
        else:
            narrative = (
                f"The borrower exhibits a strong operating footprint in the {sector} sector within {district}. "
                f"The gradient boosting pipeline classified this facility as 'Low Risk' with {conf_pct} model confidence. "
                f"Prudent balance sheet leverage alongside clean historical repayment discipline indicates solid debt service capability."
            )
            recommendation = (
                "Recommended for fast-track credit approval under standard SME commercial lending terms. "
                "Maintain standard quarterly financial covenant reviews and annual stock hypothecation audits."
            )

    elif level == "medium":
        if lang == "bn":
            narrative = (
                f"{district} অঞ্চলে অবস্থিত এই {sector} প্রতিষ্ঠানটির ঋণ আবেদন মাঝারি মাত্রার ঝুঁকির আওতাভুক্ত ({conf_pct} কনফিডেন্স)। "
                f"ব্যবসার মৌলিক ভিত্তি সক্রিয় হলেও নির্দিষ্ট কিছু আর্থিক অনুপাত এবং জামানতের তারল্য সতর্কতামূলক পর্যবেক্ষণ দাবি করে।"
            )
            recommendation = (
                "শর্তসাপেক্ষ অনুমোদন বিবেচনা করা যেতে পারে। "
                "ঋণের মূল অঙ্ক ১০% থেকে ১৫% কমিয়ে দেওয়া অথবা অতিরিক্ত ব্যক্তিগত গ্যারান্টি (Personal Guarantee) "
                "এবং বিকল্প জামানত গ্রহণের সুপারিশ করা হচ্ছে।"
            )
        else:
            narrative = (
                f"This applicant in the {sector} sector in {district} lands in the 'Medium Risk' band with {conf_pct} model confidence. "
                f"While core cash flows demonstrate solvency, specific financial ratios and collateral buffer warrant measured underwriting caution."
            )
            recommendation = (
                "Conditional approval is advised. Suggest capping credit exposure to 80-85% of requested amount, "
                "requiring promoter personal guarantee, and enforcing milestone-based disbursement."
            )

    else:  # high
        if lang == "bn":
            narrative = (
                f"আবেদনকারী প্রতিষ্ঠানটির সামগ্রিক প্রোফাইলে উচ্চমাত্রার ঋণ ঝুঁকি পরিলক্ষিত হয়েছে ({conf_pct} মডেল কনফিডেন্স)। "
                f"অতিরিক্ত দায়ভার, অপর্যাপ্ত জামানত কিংবা অতীত খেলাপির রেকর্ড বর্তমান কাঠামোর আওতায় ঋণ পরিশোধের নিশ্চয়তাকে চ্যালেঞ্জের মুখে ফেলে।"
            )
            recommendation = (
                "বিদ্যমান কাঠামোর অধীনে আবেদনটি মঞ্জুর না করার পরামর্শ দেওয়া হচ্ছে। "
                "যদি ঋণ বিবেচনা করতেই হয়, তবে ন্যূনতম ১০০% রিয়েল এস্টেট মর্টগেজ জামানত "
                "এবং বাংলাদেশ ব্যাংকের এসএমই ক্রেডিট গ্যারান্টি স্কিমের (CGAS) অন্তর্ভুক্তি বাধ্যতামূলক করা প্রয়োজন।"
            )
        else:
            narrative = (
                f"The applicant exhibits an elevated default probability risk profile ({conf_pct} model confidence). "
                f"High leverage, constrained pledged collateral, or historical credit irregularities undermine debt service certainty."
            )
            recommendation = (
                "Decline or defer standard credit sanction. In exceptional consideration, require 100%+ tangible mortgage "
                "collateral, structural facility downsizing, and enrollment under the SME Credit Guarantee Scheme."
            )

    return {
        "narrative": narrative,
        "strengths": strengths,
        "risks": risks,
        "recommendation": recommendation
    }
