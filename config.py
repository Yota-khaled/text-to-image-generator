# config.py
import os
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("⚠️ Hugging Face token not found. Please set HF_TOKEN environment variable.")


headers = {"Authorization": f"Bearer {HF_TOKEN}"}
