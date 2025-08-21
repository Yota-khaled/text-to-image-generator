# utils.py
import requests
import os
from config import API_URL, headers

def generate_image(prompt: str):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    if response.status_code != 200:
        return None, response.text
    return response.content, None

def save_image(image_bytes, filename="generated.png"):
    os.makedirs("photos", exist_ok=True)
    file_path = os.path.join("photos", filename)
    with open(file_path, "wb") as f:
        f.write(image_bytes)
    return file_path
