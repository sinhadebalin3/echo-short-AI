from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from utils.preprocessing import preprocess_image
from utils.mapping import map_waste_category, suggest_bin
from utils.advice import get_recycling_advice
from model.predictor import predict_image

router = APIRouter()

@router.post("/predict")
async def predict_waste(file: UploadFile = File(...)):
    """
    1 & 8. Image Input API & API Response Format
    - Accepts an image via a POST request file upload.
    - Validates file, orchestrates preprocessing, AI prediction, and formatting.
    - Returns JSON response with waste type, confidence, bin, and advice.
    """
    if not file.content_type.startswith("image/"):
        return JSONResponse(status_code=400, content={"error": "Please upload a valid image file."})
    
    # Read the image bytes from the request
    image_bytes = await file.read()
    
    try:
        # Step 1: Preprocess the input image
        processed_tensor = preprocess_image(image_bytes)
        
        # Step 2: Get AI prediction
        raw_label, confidence = predict_image(processed_tensor)
        
        # Step 3: Map to our specific waste categories
        waste_category = map_waste_category(raw_label)
        
        # Step 4: Generate suggestions and advice
        bin_suggestion = suggest_bin(waste_category)
        advice = get_recycling_advice(waste_category)
        
        # Format confidence to percentage
        confidence_percent = f"{confidence * 100:.1f}%"
        
        # Step 5: Return exactly the format requested
        return {
            "waste_type": waste_category.capitalize(),
            "raw_detection": raw_label.capitalize(), # Extra info for context
            "confidence": confidence_percent,
            "bin": bin_suggestion,
            "advice": advice
        }
        
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
