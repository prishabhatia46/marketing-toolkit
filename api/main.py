from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import os
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from sentiment_analyzer import predict_sentiment
from post_generator import generate_instagram_post, generate_whatsapp_message

app = FastAPI(title="BizGenius Marketing Toolkit API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class SentimentRequest(BaseModel):
    text: str

class PostRequest(BaseModel):
    product_name: str
    description: str
    price: int = None
    platform: str = "instagram"

@app.get("/")
def home():
    return {"message": "BizGenius Marketing Toolkit API", "status": "running"}

@app.post("/analyze-sentiment")
def analyze(request: SentimentRequest):
    result = predict_sentiment(request.text)
    return result

@app.post("/generate-post")
def create_post(request: PostRequest):
    if request.platform == "instagram":
        post = generate_instagram_post(
            request.product_name,
            request.description,
            request.price
        )
    else:
        post = generate_whatsapp_message(
            request.product_name,
            request.description,
            request.price
        )
    return {"platform": request.platform, "post": post}