IMAGE_PROMPT = """
Analyze the provided image and generate a new, visually stunning, high-quality image inspired by it.
The new image should capture the essence, style, and mood of the original but be a unique creation.
The output must be only the image.
"""

# Prompt for when only text is provided
TEXT_PROMPT = """
Content Idea: “Motivational Monday” Series

Purpose: Boost engagement at the start of the week with short, relatable motivational content.

Sample Caption:
"New week. New energy. New goals. ✨
Remember, even small steps count—keep moving forward!"

Image Concept:

Minimalist design with a sunrise background.

A silhouette of a person climbing stairs or a mountain.

Bold text overlay: “Small Steps, Big Changes”.

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

