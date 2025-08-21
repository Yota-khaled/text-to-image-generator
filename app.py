import streamlit as st
from utils import generate_image, save_image

st.set_page_config(page_title="Text-to-Image Generator", page_icon="🎨", layout="centered")

st.title("🎨 AI Text-to-Image Generator")
st.markdown("Generate stunning images from your text prompts using **Stable Diffusion XL**")

if "prompt" not in st.session_state:
    st.session_state.prompt = ""

if "image_bytes" not in st.session_state:
    st.session_state.image_bytes = None

if "history" not in st.session_state:
    st.session_state.history = []


st.session_state.prompt = st.text_area("✏️ Enter your text prompt:", st.session_state.prompt)

if st.session_state.history:
    selected = st.selectbox("📜 Or pick from history:", st.session_state.history)
    if st.button("Use Selected Prompt"):
        st.session_state.prompt = selected

# generate
if st.button("Generate Image"):
    with st.spinner("⚡ Generating... please wait..."):
        image_bytes, error = generate_image(st.session_state.prompt)

        if error:
            st.error(f"Request failed: {error}")
        elif image_bytes:
            st.session_state.image_bytes = image_bytes
            save_image(image_bytes, filename="generated.png")

            if st.session_state.prompt not in st.session_state.history:
                st.session_state.history.append(st.session_state.prompt)

# show + download
if st.session_state.image_bytes:
    st.image(st.session_state.image_bytes, caption="🖼️ Generated Image", use_container_width=True)

    st.download_button(
        label="📥 Download Image",
        data=st.session_state.image_bytes,
        file_name="generated.png",
        mime="image/png"
    )
