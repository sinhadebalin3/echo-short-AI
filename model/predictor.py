from model.model_loader import load_ai_model
from tensorflow.keras.applications.mobilenet import decode_predictions

def predict_image(processed_img) -> tuple:
    """
    4. Prediction Function
    - Passes the preprocessed tensor format image to the AI model.
    - Returns the most likely label and its confidence probability.
    """
    model = load_ai_model()
    
    # Get predictions
    predictions = model.predict(processed_img)
    
    # decode_predictions returns a list of lists: [[(class_id, class_name, probability), ...]]
    # We grab the top 1 prediction
    results = decode_predictions(predictions, top=1)[0]
    
    top_label = results[0][1]
    confidence_score = float(results[0][2])
    
    # Replace underscores with spaces for readability
    top_label = top_label.replace("_", " ")
    
    return top_label, confidence_score
