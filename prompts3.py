IMAGE_PROMPT = """
Act as a luxury jewellery brand’s creative director and social media strategist. Based on the jewellery item image provided, generate a complete Instagram post that is both trendy and brand-consistent.

you have to create an image with the given description and the item image which you include should match 100% to the item image i have provide to you.

Image: A photorealistic, high-end Instagram-ready image or lifestyle render of the jewellery item. Feel free to follow or creatively adapt current visual trends — such as:

Natural light + editorial shadows

"Messy luxury" flat lays

Moody minimalism or bold color-blocked backgrounds

Viral aesthetic themes (e.g. coquette, quiet luxury, mob wife, etc.)

Add props or backdrops to elevate story (e.g. silk fabric, perfume bottle, mirror reflection, etc.
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
Act as a luxury jewellery brand’s creative director and social media strategist. Based on the jewellery item image provided, generate a complete Instagram post that is both trendy and brand-consistent.

Create:

Image: A photorealistic, high-end Instagram-ready image or lifestyle render of the jewellery item. Feel free to follow or creatively adapt current visual trends — such as:

Natural light + editorial shadows

"Messy luxury" flat lays

Moody minimalism or bold color-blocked backgrounds

Viral aesthetic themes (e.g. coquette, quiet luxury, mob wife, etc.)

Add props or backdrops to elevate story (e.g. silk fabric, perfume bottle, mirror reflection, etc.

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

