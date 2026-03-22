def get_recycling_advice(category: str) -> str:
    """
    7. Recycling Advice Function
    - Returns useful suggestion text based on category.
    """
    advice_dict = {
        "plastic": "Ensure the plastic is clean and empty before recycling. Crush bottles to save space.",
        "metal": "Rinse out cans. Do not crush aluminum cans if your local facility prefers them whole.",
        "paper": "Keep paper dry. Flatten cardboard boxes. Do not recycle greasy pizza boxes.",
        "glass": "Remove lids. Do not mix broken glass or window glass with regular bottle glass.",
        "organic": "Compost this! Great for soil. Do not include dairy or meats in standard compost.",
        "unknown": "We couldn't clearly identify this object. When in doubt, throw it out to prevent recycling contamination."
    }
    return advice_dict.get(category, "Please check local guidelines.")
