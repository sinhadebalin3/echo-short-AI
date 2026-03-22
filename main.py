from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import predict
from model.model_loader import load_ai_model

app = FastAPI(title="Smart Waste Management API", version="1.0")

# Setup CORS to allow our Flutter frontend to access it
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routes
app.include_router(predict.router)

# Pre-load the ML model when the app starts
@app.on_event("startup")
async def startup_event():
    load_ai_model()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Waste Management AI API!"}
