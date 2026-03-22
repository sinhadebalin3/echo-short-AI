def map_waste_category(label: str) -> str:
    """
    5. Waste Mapping Function
    - Since we are using standard ImageNet weights, it recognizes a lot of objects.
    - We group some common ImageNet labels into our 5 waste categories.
    - For a real hackathon, you'd train a custom model, but this works nicely for a demo!
    """
    label = label.lower()
    
    plastic_keywords = ['bottle', 'plastic', 'cup', 'jug', 'water']
    metal_keywords = ['can', 'tin', 'aluminum']
    paper_keywords = ['paper', 'cardboard', 'box', 'envelope', 'carton']
    glass_keywords = ['glass', 'jar', 'wine', 'beer']
    organic_keywords = ['apple', 'banana', 'orange', 'fruit', 'food', 'vegetable', 'leaf']
    
    for kw in plastic_keywords:
        if kw in label: return "plastic"
    for kw in metal_keywords:
        if kw in label: return "metal"
    for kw in paper_keywords:
        if kw in label: return "paper"
    for kw in glass_keywords:
        if kw in label: return "glass"
    for kw in organic_keywords:
        if kw in label: return "organic"
        
    return "unknown"

def suggest_bin(category: str) -> str:
    """
    6. Bin Suggestion Function
    - Maps category to standard bin color.
    """
    bins = {
        "plastic": "Blue Bin (Recyclable)",
        "metal": "Blue Bin (Recyclable)",
        "paper": "Blue Bin / Yellow Bin",
        "glass": "Green Bin (Glass)",
        "organic": "Brown/Green Bin (Compost)",
        "unknown": "Black Bin (General Waste)"
    }
    return bins.get(category, "Black Bin (General Waste)")
