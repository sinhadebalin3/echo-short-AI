import tensorflow as tf
from tensorflow.keras.applications import MobileNet

# Global variable to hold the model in memory
model = None

def load_ai_model():
    """
    3. Model Loading Function
    - Loads MobileNet with ImageNet weights.
    - We use a pre-trained model because it already 'knows' how to extract rich image features 
      without requiring hours of training and thousands of images. Perfect for a fast hackathon demo!
    """
    global model
    if model is None:
        print("Loading MobileNet model...")
        model = MobileNet(weights='imagenet')
        print("Model loaded successfully!")
    return model
