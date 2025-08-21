# 🎨 AI Text-to-Image Generator

Generate stunning images from your text prompts using **Stable Diffusion XL** via Hugging Face API 🚀  
Built with **Streamlit** for an interactive UI.

---

## ⚡ Features

- Enter any text prompt and generate AI images instantly
- View the generated image inside the app
- Download your generated images with one click
- Saved images are stored inside a `photos/` folder automatically (folder will be created if it does not exist)
- Keeps your last entered prompt & generated image using `st.session_state`

---

## 📦 Installation

1. Clone this repository:

```bash
git clone https://github.com/Yota-khaled/text-to-image-generator.git
cd text-to-image-generator
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your Hugging Face token securely using a `.env` file:

```env
HUGGINGFACE_TOKEN=your_token_here
```

4. Load the token inside `utils.py` using `python-dotenv`:

```python
from dotenv import load_dotenv
import os

load_dotenv()
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
```

5. Run the app:

```bash
streamlit run app.py 
```

---

## 🔑 Hugging Face Token Setup

1. Go to [Hugging Face Tokens](https://huggingface.co/settings/tokens)
2. Create a new **Read** token
3. Save it in a `.env` file and load it in `utils.py` to keep your token secure

---

## 📂 Project Structure

```
📦 text-to-image-generator
 ┣ photos/           # Generated images are saved here
 ┣ app.py            # Streamlit UI
 ┣ utils.py          # API request + save logic
 ┣ requirements.txt  # Dependencies
 ┗ README.md         # Documentation
```

---

## 🖼️ Example Prompt Ideas

* "A futuristic city in the clouds, ultra realistic"
* "A watercolor painting of a cozy cabin in the snowy forest"
* "A cyberpunk cat wearing neon sunglasses"
* "A fantasy castle floating on an island in the sky"
* "An astronaut riding a horse on Mars"

---

