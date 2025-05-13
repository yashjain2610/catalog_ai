import streamlit as st
import base64
from PIL import Image
import io
from io import BytesIO
import google.generativeai as genai
from utils2 import *
import os
from dotenv import load_dotenv

from prompts2 import *

load_dotenv()

st.set_page_config(
    page_title="Gemini Vision Prompting",
    page_icon="💎",
    layout="wide"
)

st.title("💎 Gemini Vision Prompting with Image + Prompts")
st.markdown("Upload an image and input prompts to get generated text and visuals using Gemini 2.0 Flash Image Generation model")


PROMPT_LIST = [
    white_bgd_prompt,
    multicolor_1_prompt,
    multicolor_2_prompt,
    props_img_prompt,
    hand_prompt,
]
uploaded_images = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg", "webp"],accept_multiple_files=True , key="up1")

for uploaded_image in uploaded_images:
        image = Image.open(uploaded_image)
        filename = uploaded_image.name

        st.markdown(f"## 🖼️ Uploaded Image: `{filename}`")
        st.image(image, caption=filename, use_container_width=300)



generate = st.button("generate for earrings")





if "responses" not in st.session_state:
    st.session_state["responses"] = {}

if generate:
    if uploaded_images is not None:
        for uploaded_image in uploaded_images:
            image = Image.open(uploaded_image)
            filename = uploaded_image.name

            if filename not in st.session_state["responses"]:
                st.info(f"Generating for {filename} ...")
                responses = get_gemini_responses("analyse the image",image, PROMPT_LIST)
                st.session_state["responses"][filename] = responses



if uploaded_images is not None:
    for uploaded_image in uploaded_images:
        image = Image.open(uploaded_image)
        filename = uploaded_image.name

        # st.markdown(f"## 🖼️ Uploaded Image: `{filename}`")
        # st.image(image, caption=filename, use_container_width=300)

        if filename in st.session_state["responses"]:
            responses = st.session_state["responses"][filename]

            cols = st.columns(len(responses))

            for i, (col, item) in enumerate(zip(cols, responses)):
                try:
                    # There is always one image in item["images"]
                    img_bytes = item["images"][0]

                    gen_image = Image.open(io.BytesIO(img_bytes))
                    gen_image = resize_img(gen_image)

                    img_buffer = io.BytesIO()
                    gen_image.save(img_buffer, format="PNG")
                    resized_img_bytes = img_buffer.getvalue()

                    with col:
                        st.markdown(f"### Image Set {i+1}")  # title inside each column
                        st.image(resized_img_bytes, use_container_width=True)

                        download_col, regen_col = st.columns([1, 1])

                        with download_col:
                            st.download_button(
                                label="⬇️",
                                data=resized_img_bytes,
                                file_name=f"{filename}_prompt{i}.png",
                                mime="image/png",
                                key=f"download_{filename}_{i}"
                            )

                        with regen_col:
                            if st.button("🔁", key=f"regen_{filename}_{i}"):
                                new_response = get_gemini_responses("analyse the image", image, [PROMPT_LIST[i]])[0]
                                st.session_state["responses"][filename][i] = new_response
                                st.rerun()

                except Exception as e:
                    col.error(f"Error displaying image {i + 1}: {e}")



BRACELET_PROMPT_LIST = [
    white_bgd_bracelet_prompt,
    multicolor_1_bracelet_prompt,
    multicolor_2_bracelet_prompt,
    props_img_bracelet_prompt,
    hand_bracelet_prompt,
]

generate_bracelet = st.button("generate for bracelets")

if "bracelet_responses" not in st.session_state:
    st.session_state["bracelet_responses"] = {}

if generate_bracelet:
    if uploaded_images is not None:
        for uploaded_image in uploaded_images:
            image = Image.open(uploaded_image)
            filename = uploaded_image.name

            if filename not in st.session_state["bracelet_responses"]:
                st.info(f"Generating bracelets for {filename} ...")
                responses = get_gemini_responses("analyse the image", image, BRACELET_PROMPT_LIST)
                st.session_state["bracelet_responses"][filename] = responses

# display uploaded images + generated bracelet sets
if uploaded_images is not None:
    for uploaded_image in uploaded_images:
        image = Image.open(uploaded_image)
        filename = uploaded_image.name

        # st.markdown(f"## 🖼️ Uploaded Image (Bracelets): `{filename}`")
        # st.image(image, caption=filename, use_container_width=300)

        if filename in st.session_state["bracelet_responses"]:
            responses = st.session_state["bracelet_responses"][filename]
            cols = st.columns(len(responses))

            for i, (col, item) in enumerate(zip(cols, responses)):
                try:
                    img_bytes = item["images"][0]
                    gen_image = Image.open(io.BytesIO(img_bytes))
                    gen_image = resize_img(gen_image)

                    img_buffer = io.BytesIO()
                    gen_image.save(img_buffer, format="PNG")
                    resized_img_bytes = img_buffer.getvalue()

                    with col:
                        st.markdown(f"### Bracelet Image Set {i+1}")
                        st.image(resized_img_bytes, use_container_width=True)

                        download_col, regen_col = st.columns([1, 1])
                        with download_col:
                            st.download_button(
                                label="⬇️",
                                data=resized_img_bytes,
                                file_name=f"{filename}_bracelet_prompt{i}.png",
                                mime="image/png",
                                key=f"download_bracelet_{filename}_{i}"
                            )
                        with regen_col:
                            if st.button("🔁", key=f"regen_bracelet_{filename}_{i}"):
                                new_response = get_gemini_responses("analyse the image", image, [BRACELET_PROMPT_LIST[i]])[0]
                                st.session_state["bracelet_responses"][filename][i] = new_response
                                st.rerun()

                except Exception as e:
                    col.error(f"Error displaying bracelet image {i + 1}: {e}")



NECKLACE_PROMPT_LIST = [
    white_bgd_necklace_prompt,
    multicolor_1_necklace_prompt,
    multicolor_2_necklace_prompt,
    props_img_necklace_prompt,
    hand_necklace_prompt,
    neck_necklace_prompt
]

generate_necklace = st.button("generate for necklaces")

if "necklace_responses" not in st.session_state:
    st.session_state["necklace_responses"] = {}

if generate_necklace:
    if uploaded_images is not None:
        for uploaded_image in uploaded_images:
            image = Image.open(uploaded_image)
            filename = uploaded_image.name

            if filename not in st.session_state["necklace_responses"]:
                st.info(f"Generating necklaces for {filename} ...")
                responses = get_gemini_responses("analyse the image", image, NECKLACE_PROMPT_LIST)
                st.session_state["necklace_responses"][filename] = responses

# display uploaded images + generated necklace sets
if uploaded_images is not None:
    for uploaded_image in uploaded_images:
        image = Image.open(uploaded_image)
        filename = uploaded_image.name

        if filename in st.session_state["necklace_responses"]:
            responses = st.session_state["necklace_responses"][filename]
            cols = st.columns(len(responses))

            for i, (col, item) in enumerate(zip(cols, responses)):
                try:
                    img_bytes = item["images"][0]
                    gen_image = Image.open(io.BytesIO(img_bytes))
                    gen_image = resize_img(gen_image)

                    img_buffer = io.BytesIO()
                    gen_image.save(img_buffer, format="PNG")
                    resized_img_bytes = img_buffer.getvalue()

                    with col:
                        st.markdown(f"### Necklace Image Set {i+1}")
                        st.image(resized_img_bytes, use_container_width=True)

                        download_col, regen_col = st.columns([1, 1])
                        with download_col:
                            st.download_button(
                                label="⬇️",
                                data=resized_img_bytes,
                                file_name=f"{filename}_necklace_prompt{i}.png",
                                mime="image/png",
                                key=f"download_necklace_{filename}_{i}"
                            )
                        with regen_col:
                            if st.button("🔁", key=f"regen_necklace_{filename}_{i}"):
                                new_response = get_gemini_responses(
                                    "analyse the image",
                                    image,
                                    [NECKLACE_PROMPT_LIST[i]]
                                )[0]
                                st.session_state["necklace_responses"][filename][i] = new_response
                                st.rerun()

                except Exception as e:
                    col.error(f"Error displaying necklace image {i + 1}: {e}")


