import streamlit as st
from utils3 import *
from prompts3 import *
import io
from io import BytesIO
# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="Social Media Post Generator",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="auto",
)

if 'generated_content' not in st.session_state:
    st.session_state.generated_content = []
if 'prompts_list' not in st.session_state:
    st.session_state.prompts_list = []
if 'style_image_bytes' not in st.session_state:
    st.session_state.style_image_bytes = None

# --- Regeneration Callback Function ---
def handle_regenerate(index):
    """
    Called when a 'Regenerate' button is clicked.
    It re-runs the Gemini API for a single prompt and updates the content in session state.
    """
    with st.spinner(f"Regenerating image {index + 1}..."):
        try:
            # Get the specific prompt for the image we want to regenerate
            prompt = st.session_state.prompts_list[index]
            
            # Use the stored style image if it exists
            style_image = st.session_state.style_image_bytes
            # if style_image:
            #      style_image = Image.open(io.BytesIO(style_image))

            # Call the API for just one prompt
            new_content_list = get_gemini_responses("test", style_image, [prompt])
            
            if new_content_list:
                # Replace the old response object with the new one at the correct index
                st.session_state.generated_content[index] = new_content_list[0]
            else:
                st.warning("Regeneration did not return any content.")
        except Exception as e:
            st.error(f"An error occurred during regeneration: {e}")





# --- Main Application UI ---
st.title("🚀 AI-Powered Social Media Post Generator")
st.markdown(
    "Generate engaging social media posts with the power of Gemini. "
    "Upload an image, enter some text, or do both!"
)

# --- Input Fields ---
st.header("1. Provide overview of your post")

# Text Input
user_text = st.text_area(
    "Enter a topic, keywords, or a draft for your post:",
    height=150,
    key="text_input_1",
    placeholder="e.g., A new product launch for sustainable coffee cups"
)

st.header("2. provide description of first image")

image_text_1= st.text_area(
    "Enter a topic, keywords, or a draft for your post:",
    height=68,
    key="text_input_2",
    placeholder="e.g., A new product launch for sustainable coffee cups"
)

st.header("3. provide description of second image")

image_text_2= st.text_area(
    "Enter a topic, keywords, or a draft for your post:",
    height=68,
    key="text_input_3",
    placeholder="e.g., A new product launch for sustainable coffee cups"
)

st.header("4. provide description of third image")

image_text_3= st.text_area(
    "Enter a topic, keywords, or a draft for your post:",
    height=68,
    key="text_input_4",
    placeholder="e.g., A new product launch for sustainable coffee cups"
)

use_resize = st.checkbox("Use 1:1", value=False)
use_resize2 = st.checkbox("Use 3:4", value=False)
use_resize3 = st.checkbox("Use 9:16", value=False)



# Image Input
uploaded_file = st.file_uploader(
    "Upload an image (optional):",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image.", use_container_width=True)

# --- Generate Button and Logic ---
st.header("2. Generate Your Post")
generate_button = st.button("✨ Generate Post", type="primary")

if generate_button:
    # --- Input validation ---
    image_descriptions = [desc for desc in [image_text_1, image_text_2, image_text_3] if desc.strip()]
    if uploaded_file is None and not user_text:
        st.error("Please provide an image, text, or both to generate a post.")
    else:
        with st.spinner("Generating your social media post... This might take a moment."):
            try:
                # --- Prepare inputs for the model ---
                if uploaded_file:
                    image_bytes = Image.open(uploaded_file)
                    st.session_state.style_image_bytes = image_bytes
                else:
                    image_bytes = None
                prompt = ""
                prompts_list = []

                if uploaded_file and user_text:
                    # Case 1: Both image and text are provided
                    st.info("Using both image and text for generation.")
                    prompt = IMAGE_AND_TEXT_PROMPT.format(user_text=user_text)

                elif uploaded_file:
                    # Case 2: Only image is provided
                    st.info("Using the uploaded image for generation.")
                    prompt = IMAGE_PROMPT

                elif user_text:
                    # Case 3: Only text is provided
                    st.info("Using the provided text for generation.")
                    #prompt = TEXT_PROMPT.format(user_text=user_text)
                    for desc in image_descriptions:
                        prompt = THEMED_IMAGE_PROMPT.format(
                            overview_text=user_text,
                            image_description=desc
                        )
                        prompts_list.append(prompt)
                

                # --- Call the Gemini API ---
                if len(prompts_list) > 0:
                    st.session_state.prompts_list = prompts_list
                    generated_content = get_gemini_responses("test",image_bytes,prompts_list)
                else:
                    st.session_state.prompts_list = [prompt]
                    generated_content = get_gemini_responses("text", image_bytes, [prompt])
                
                st.session_state.generated_content = generated_content

                                # --- Display the results ---
            #     if not generated_content:
            #         st.warning("The model did not return any content. Please try a different prompt or image.")
            #     else:
            #         st.success("Content generated successfully! 🎉")

            #         # Loop through each response object (your function returns a list)
            #         for i, response in enumerate(generated_content):

            #             # Display generated text if it exists
            #             if response.get("text"):
            #                 st.subheader(f"Generated Caption/Text {i+1}:")
            #                 st.markdown(response["text"]) # Using markdown for better formatting

            #             # Display generated images if they exist
            #             if response.get("images"):
            #                 st.subheader(f"Generated Image(s) for Prompt {i+1}:")
            #                 # Loop through each image in the response
            #                 for j, img_bytes in enumerate(response["images"]):

            #                     gen_image = Image.open(io.BytesIO(img_bytes))
            #                     gen_image = resize_img(gen_image)

            #                     img_buffer = io.BytesIO()
            #                     gen_image.save(img_buffer, format="PNG")
            #                     resized_img_bytes = img_buffer.getvalue()
            #                     img_bytes = resized_img_bytes

            #                     # Use columns to display image and download button side-by-side or neatly
            #                     col1, col2 = st.columns([4, 1])

            #                     with col1:
            #                         # Display the image
            #                         st.image(
            #                             img_bytes,
            #                             caption=f"Generated Image {j+1}",
            #                             use_container_width=True
            #                         )

            #                     with col2:
            #                         # Add a download button for the image
            #                         st.download_button(
            #                             label="Download",
            #                             data=img_bytes,
            #                             file_name=f"generated_image_{i+1}_{j+1}.png",
            #                             mime="image/png",
            #                             key=f"download_{i}_{j}" # Unique key for each button
            #                         )
            #             st.divider() # Add a separator between different prompt responses

            except Exception as e:
                 st.error(f"An error occurred during generation: {e}")

if st.session_state.generated_content:
    st.success("Content generated successfully! 🎉")

    # Loop through each response object stored in the session state
    for i, response in enumerate(st.session_state.generated_content):
        if response.get("images"):
            st.subheader(f"Generated Image {i+1}:")
            # There can be multiple images per response, but we'll assume one for simplicity
            for j, img_bytes in enumerate(response["images"]):
                gen_image = Image.open(io.BytesIO(img_bytes))
                gen_image = resize_img(gen_image,use_resize,use_resize2,use_resize3)

                img_buffer = io.BytesIO()
                gen_image.save(img_buffer, format="PNG")
                img_bytes = img_buffer.getvalue()

                # Use columns for a neat layout
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.image(
                        img_bytes,
                        #caption=f"Generated from: \"{st.session_state.prompts_list[i].split('**Specific Image to Generate:** ')[1].split('**Instructions:**')[0].strip()}\"",
                        use_container_width=True
                    )
                with col2:
                    st.download_button(
                        label="Download",
                        data=img_bytes,
                        file_name=f"generated_image_{i+1}_{j+1}.png",
                        mime="image/png",
                        key=f"download_{i}_{j}"
                    )
                    # REGENERATE BUTTON: Calls the handler function when clicked
                    st.button(
                        label="Regenerate",
                        key=f"regenerate_{i}_{j}",
                        on_click=handle_regenerate,
                        args=(i,) # Pass the index of the image to regenerate
                    )
            st.divider()



# --- Footer ---
st.markdown("---")
st.markdown("Powered by Google Gemini")