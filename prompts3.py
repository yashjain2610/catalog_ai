IMAGE_PROMPT = """
Analyze the provided image and generate a new, visually stunning, high-quality image inspired by it.
The new image should capture the essence, style, and mood of the original but be a unique creation.
The output must be only the image.
"""

# Prompt for when only text is provided
TEXT_PROMPT = """
Based on the description, generate a visually stunning, high-quality image perfect for a social media post.
The style should be vibrant, engaging, and directly related to the text.
The output must be only the image.

Description: "{user_text}"
"""

# Prompt for when both an image and text are provided
IMAGE_AND_TEXT_PROMPT = """
Create a new, visually stunning, high-quality image that combines the theme of the uploaded picture with the following description.
The new image should be a cohesive blend of both inputs, creating a unique visual narrative.
The output must be only the image.

Description: "{user_text}"
"""

THEMED_IMAGE_PROMPT = """
                You are an AI image generator creating a set of images for a single, cohesive social media post.

                **Overall Post Theme/Style:** "{overview_text}"
                **Specific Image to Generate:** "{image_description}"

                **Instructions:**
                1. Generate a high-quality image based on the **Specific Image to Generate** description.
                2. CRITICAL: Ensure the generated image's style, mood, and color palette strictly adhere to the **Overall Post Theme/Style**. All images in this set must look like they belong together.
                3. If a style reference image is provided, use its aesthetic as the primary inspiration.
                4. The output must be only the image, with no additional text.
"""

