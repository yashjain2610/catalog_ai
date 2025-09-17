import streamlit as st
import os
import base64
import openpyxl
from prompts import *
import random
from PIL import Image , ImageOps
from io import BytesIO
from google import genai
from google.genai import types
from google.api_core import exceptions as google_exceptions
import itertools
import grpc

from dotenv import load_dotenv

load_dotenv()

# Configure the Gemini API key
# # Make sure to set the GOOGLE_API_KEY environment variable
# try:
#     genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
# except AttributeError as e:
#     # This error can occur if the environment variable is not set.
#     # Provide a helpful message to the user.
#     raise ValueError("GOOGLE_API_KEY environment variable not set. Please set it to your API key.") from e

API_KEYS = [
    os.getenv("GOOGLE_API_KEY"),
    os.getenv("GOOGLE_API_KEY2"),
    os.getenv("GOOGLE_API_KEY3"),
    os.getenv("GOOGLE_API_KEY4"),
]

#print(API_KEYS)
clients = [genai.Client(api_key=key) for key in API_KEYS]
client_cycle = itertools.cycle(clients)



def _is_quota_exceeded(err) -> bool:
    # HTTP‐style 429
    if getattr(err, 'code', None) == 429:
        return True

    # grpc.RpcError
    if isinstance(err, grpc.RpcError) and err.code() == grpc.StatusCode.RESOURCE_EXHAUSTED:
        return True

    # Google API exception
    if isinstance(err, google_exceptions.ResourceExhausted):
        return True

    # Fallback: look for the string in the message
    msg = str(err).upper()
    if 'RESOURCE_EXHAUSTED' in msg or 'QUOTA' in msg:
        return True

    return False

def generate_with_failover(model: str, contents: list, config: types.GenerateContentConfig):
    last_exc = None

    for _ in range(len(clients)):
        client = next(client_cycle)
        try:
            return client.models.generate_content(
                model=model,
                contents=contents,
                config=config
            )
        except Exception as e:
            if _is_quota_exceeded(e):
                last_exc = e
                # optionally log which key failed here
                continue
            # if it wasn’t a quota problem, bail out
            raise

    # all keys hit quota
    raise last_exc



def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

def get_gemini_responses(input_text, image, prompts):

    all_responses = []

    for prompt in prompts:
        if image == None:
            content = [prompt]
        else:
            content = [prompt, image]
        # if prompt == models_prompt:
        #     base_model_image = get_random_model_image("model images")
        #     #model_image = get_all_model_images("sample output model")
        #     content = [prompt] + [base_model_image] + [image]

        #print(content)
        try:
            response = generate_with_failover(
                model="gemini-2.0-flash-preview-image-generation",
                contents=content,
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE']
                )
            )
        except Exception as e:
            st.error(f"All API-keys exhausted or fatal error: {e}")
            break

        structured_response = {
            "prompt": prompt,
            "text": "",
            "images": []
        }

        for part in response.candidates[0].content.parts:
            if hasattr(part, "text") and part.text:
                structured_response["text"] += part.text.strip()
            elif hasattr(part, "inline_data") and part.inline_data:
                structured_response["images"].append(part.inline_data.data)

        all_responses.append(structured_response)

    #print(all_responses)
    return all_responses


def resize_img(image,one,three,nine):
    width = 0
    height = 0
    if one:
        width = 1000
        height = 1000
    elif three:
        width = 1080
        height = 1350
    elif nine:
        width = 1080
        height = 1920

    img_square = ImageOps.pad(image, (max(image.size), max(image.size)), color=(255, 255, 255))

# Resize to 2000x2000
    img_resized = img_square.resize((width, height), Image.Resampling.LANCZOS)

# Save the result
    return img_resized
