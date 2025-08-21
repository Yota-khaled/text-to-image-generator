# 🎨 AI Text-to-Image Generator

Generate stunning images from your text prompts using **Stable Diffusion
XL** via Hugging Face API 🚀\
Built with **Streamlit** for an interactive UI.

------------------------------------------------------------------------

## ⚡ Features

-   Enter any text prompt and generate AI images instantly
-   View the generated image inside the app
-   Download your generated images with one click
-   Saved images stored inside a `photos/` folder automatically
-   Keeps your last entered prompt & generated image using
    `st.session_state`

------------------------------------------------------------------------

## 📦 Installation

1.  Clone this repository:

    ``` bash
    git clone https://github.com/Yota-khaled/text-to-image-app.git
    cd text-to-image-app
    ```

2.  Install dependencies:

    ``` bash
    pip install -r requirements.txt
    ```

3.  Create a file called **utils.py** and add your Hugging Face API
    logic inside it (already provided in repo).\
    Make sure you have your Hugging Face token saved securely.

4.  Run the app:

    ``` bash
    streamlit run app.py
    ```

------------------------------------------------------------------------

## 🔑 Hugging Face Token Setup

1.  Go to [Hugging Face Tokens](https://huggingface.co/settings/tokens)
2.  Create a new **Read** token
3.  Save it inside your `utils.py` (or use environment variables for
    security)

------------------------------------------------------------------------

## 📂 Project Structure

    📦 text-to-image-app
     ┣  photos/              # Generated images are saved here
     ┣  app.py               # Streamlit UI
     ┣  utils.py             # API request + save logic
     ┣  requirements.txt     # Dependencies
     ┗  README.md            # Documentation

------------------------------------------------------------------------

## 🖼️ Example Prompt Ideas

-   "A futuristic city in the clouds, ultra realistic"
-   "A watercolor painting of a cozy cabin in the snowy forest"
-   "A cyberpunk cat wearing neon sunglasses"
-   "A fantasy castle floating on an island in the sky"
-   "An astronaut riding a horse on Mars"

------------------------------------------------------------------------

