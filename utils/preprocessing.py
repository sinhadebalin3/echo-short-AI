import cv2
import numpy as np

def preprocess_image(image_bytes: bytes) -> np.ndarray:
    """
    1. Preprocessing Function
    - Accepts image bytes from the upload.
    - Decodes to OpenCV format.
    - Resizes to 224x224 (MobileNet standard).
    - Converts to RGB.
    - Normalizes pixel values using MobileNet's preprocess_input.
    - Expands dimensions to create a batch of 1 (tensor format).
    """
    from tensorflow.keras.applications.mobilenet import preprocess_input
    
    # Convert bytes to numpy array
    nparr = np.frombuffer(image_bytes, np.uint8)
    # Decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # Resize for MobileNet
    img = cv2.resize(img, (224, 224))
    # OpenCV uses BGR, convert to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Convert to float32
    img_array = img.astype(np.float32)
    # Expand dims: shape becomes (1, 224, 224, 3)
    img_array = np.expand_dims(img_array, axis=0)
    # Normalize using MobileNet's expected preprocessing
    return preprocess_input(img_array)
