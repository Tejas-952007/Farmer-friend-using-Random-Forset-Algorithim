FERTILIZER_RULES = {
    "rice":      {"fertilizer": "Urea + DAP",               "tip": "Apply in split doses. Avoid waterlogging during tillering."},
    "wheat":     {"fertilizer": "NPK 12-32-16",             "tip": "Apply basal dose before sowing. Top-dress with urea at crown root stage."},
    "maize":     {"fertilizer": "Urea + SSP + MOP",         "tip": "Apply phosphorus at planting. Nitrogen in 3 splits."},
    "cotton":    {"fertilizer": "NPK 15-15-15",             "tip": "Avoid excess nitrogen — causes vegetative growth over bolls."},
    "sugarcane": {"fertilizer": "Ammonium Sulphate + SSP",  "tip": "Apply in furrows at planting. Ratoon crop needs extra potassium."},
    "chickpea":  {"fertilizer": "Rhizobium inoculant + SSP","tip": "Legume — minimal nitrogen needed. Focus on phosphorus."},
    "mango":     {"fertilizer": "NPK 8-8-8 + micronutrients","tip": "Apply after harvest and before flowering."},
    "banana":    {"fertilizer": "Urea + MOP",               "tip": "Potassium is critical. Apply MOP in 4 splits over the crop cycle."},
    "grapes":    {"fertilizer": "Calcium Nitrate + K2SO4",  "tip": "Drip fertigation recommended."},
    "jute":      {"fertilizer": "Urea + SSP",               "tip": "Apply nitrogen in 2 equal splits."},
    "lentil":    {"fertilizer": "SSP + Rhizobium",          "tip": "Inoculate seeds before sowing for better nitrogen fixation."},
    "default":   {"fertilizer": "NPK 10-26-26",             "tip": "Conduct soil test for precise recommendations."},
}

def get_fertilizer_advice(crop: str) -> dict:
    return FERTILIZER_RULES.get(crop.lower().strip(), FERTILIZER_RULES["default"])
