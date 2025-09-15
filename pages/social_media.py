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

# --- Main Application UI ---
st.title("🚀 AI-Powered Social Media Post Generator")
st.markdown(
    "Generate engaging social media posts with the power of Gemini. "
    "Upload an image, enter some text, or do both!"
)

# --- Input Fields ---
st.header("1. Provide Your Input")

# Text Input
user_text = st.text_area(
    "Enter a topic, keywords, or a draft for your post:",
    height=150,
    placeholder="e.g., A new product launch for sustainable coffee cups"
)

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
    if uploaded_file is None and not user_text:
        st.error("Please provide an image, text, or both to generate a post.")
    else:
        with st.spinner("Generating your social media post... This might take a moment."):
            try:
                # --- Prepare inputs for the model ---
                if uploaded_file:
                    image_bytes = Image.open(uploaded_file)
                else:
                    image_bytes = None
                prompt = ""

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
                    prompt = TEXT_PROMPT.format(user_text=user_text)

                # --- Call the Gemini API ---
                generated_content = get_gemini_responses("test",image_bytes, [prompt])

                                # --- Display the results ---
                if not generated_content:
                    st.warning("The model did not return any content. Please try a different prompt or image.")
                else:
                    st.success("Content generated successfully! 🎉")

                    # Loop through each response object (your function returns a list)
                    for i, response in enumerate(generated_content):

                        # Display generated text if it exists
                        if response.get("text"):
                            st.subheader(f"Generated Caption/Text {i+1}:")
                            st.markdown(response["text"]) # Using markdown for better formatting

                        # Display generated images if they exist
                        if response.get("images"):
                            st.subheader(f"Generated Image(s) for Prompt {i+1}:")
                            # Loop through each image in the response
                            for j, img_bytes in enumerate(response["images"]):

                                gen_image = Image.open(io.BytesIO(img_bytes))
                                gen_image = resize_img(gen_image)

                                img_buffer = io.BytesIO()
                                gen_image.save(img_buffer, format="PNG")
                                resized_img_bytes = img_buffer.getvalue()
                                img_bytes = resized_img_bytes

                                # Use columns to display image and download button side-by-side or neatly
                                col1, col2 = st.columns([4, 1])

                                with col1:
                                    # Display the image
                                    st.image(
                                        img_bytes,
                                        caption=f"Generated Image {j+1}",
                                        use_container_width=True
                                    )

                                with col2:
                                    # Add a download button for the image
                                    st.download_button(
                                        label="Download",
                                        data=img_bytes,
                                        file_name=f"generated_image_{i+1}_{j+1}.png",
                                        mime="image/png",
                                        key=f"download_{i}_{j}" # Unique key for each button
                                    )
                        st.divider() # Add a separator between different prompt responses

            except Exception as e:
                st.error(f"An error occurred during generation: {e}")



# --- Footer ---
st.markdown("---")
st.markdown("Powered by Google Gemini")