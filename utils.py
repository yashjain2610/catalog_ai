import streamlit as st
import os
import base64
import openpyxl

import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



def get_gemini_responses(input, image, prompts):
    model = genai.GenerativeModel('gemini-2.0-flash',
                                  generation_config=genai.types.GenerationConfig(
                                      temperature=0.5,
                                      top_p=0.9,
                                      top_k=40,
                                      max_output_tokens=1024
                                  ))
    all_responses = []
    for prompt in prompts:
        response = model.generate_content([input, image[0], prompt])
        for part in response.parts:
            if part.text:
                all_responses.append(part.text)
    #print(all_responses)
    return all_responses

def get_gemini_responses_multi_image(text_input, image_list, prompts):
    """
    Sends a request to the Gemini 1.5 Flash model with text, multiple images, 
    and a series of prompts.

    Args:
        text_input (str): The common text input to be included in all prompts.
        image_list (list): A list of image objects (e.g., from PIL.Image.open()).
        prompts (list): A list of string prompts to be sent to the model.

    Returns:
        list: A list of text responses from the model for each prompt.
    """
    # Configure the generative model with your desired settings
    model = genai.GenerativeModel('gemini-2.0-flash',
                                  generation_config=genai.types.GenerationConfig(
                                      temperature=0.5,
                                      top_p=0.9,
                                      top_k=40,
                                      max_output_tokens=1024
                                  ))
    
    all_responses = []
    
    # Iterate through each prompt provided
    for prompt in prompts:
        # The key change is here: we construct the content list by combining
        # the initial text, all images from the image_list, and the current prompt.
        # The model can accept multiple images in the input list.
        content_parts = [text_input] + image_list + [prompt]
        
        try:
            # Generate content using the combined list of parts
            response = model.generate_content(content_parts)
            
            # Extract text from the response parts
            for part in response.parts:
                if part.text:
                    all_responses.append(part.text)
        except Exception as e:
            print(f"An error occurred while processing a prompt: {e}")
            all_responses.append(f"Error: {e}")
            
    return all_responses

def get_gemini_dims_responses(input, image, prompts):
    model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20',
                                  generation_config=genai.types.GenerationConfig(
                                      temperature=0.5,
                                      top_p=0.9,
                                      top_k=40,
                                      max_output_tokens=512
                                  ))
    all_responses = []
    for prompt in prompts:
        response = model.generate_content([input, image[0], prompt])
        # print(response)
        for part in response.parts:
            if part.text:
                all_responses.append(part.text)
    # print(all_responses)
    return all_responses[0]

# def input_image_setup(uploaded_file):
#     if uploaded_file is not None:
#         bytes_data = uploaded_file.getvalue()
#         image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]
#         return image_parts
#     else:
#         raise FileNotFoundError("No file uploaded")
    
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
def input_image_setup_local(image_path):
    with open(image_path, "rb") as img_file:
        bytes_data = img_file.read()
        mime_type = "image/jpeg" if image_path.endswith(".jpg") or image_path.endswith(".jpeg") else "image/png"
        image_parts = [{"mime_type": mime_type, "data": bytes_data}]
        return image_parts

def encode_image(uploaded_image):
    img_bytes = uploaded_image.read()
    return base64.b64encode(img_bytes).decode("utf-8")