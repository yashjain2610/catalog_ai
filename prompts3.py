IMAGE_PROMPT = """
Act as a luxury jewellery brand’s creative director and social media strategist. Based on the jewellery item image provided, generate a complete Instagram post that is both trendy and brand-consistent.

you have to create an image with the given description and the item image which you include should match 100% to the item image i have provide to you.

Design a lifestyle-oriented social media post using the uploaded jewellery product.
Place the piece in a real-life context — near fabrics, floral props, or elegant table setups — to create mood and relatability.
Lighting should be natural and warm, capturing a candid, aspirational vibe.
Style: Soft, graceful, and aspirational.
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


PROMPT1_IMG = """
Create a modern, minimal Instagram post for a jewellery brand using the uploaded product image.
Avoid plain or flat backgrounds — instead, style the jewellery against naturally textured settings such as soft sand, linen fabric, or stone surfaces.
Use warm neutral tones like beige, ivory, or muted gold, with soft directional lighting that enhances the jewellery’s shine.
Keep the frame clean with ample breathing space, gentle shadows, and subtle organic patterns.
The final image should feel sophisticated, natural, and editorial — embodying understated luxury with a refined depth.
"""

PROMPT2_IMG = """
Design a lifestyle-inspired Instagram post using the uploaded jewellery image.
Place the jewellery in a warm, organic environment — near soft fabrics, ceramics, or minimal props that reflect everyday elegance.
Maintain a modern, premium tone with natural light and warm highlights.
Ensure the overall layout feels relaxed yet aspirational, blending lifestyle storytelling with high-end simplicity.
The mood should be elegant, relatable, and effortlessly luxurious.
"""

PROMPT3_IMG = """
Generate a product-focused Instagram post for a high-end jewellery brand using the uploaded image.
Keep the jewellery as the hero element, styled on a minimal but rich background such as velvet, marble, or linen.
Use soft golden light and close-up framing to capture the craftsmanship, gemstone texture, and fine detailing.
Maintain balanced negative space around the product to give it a luxury, editorial feel.
The post should exude premium sophistication and quiet confidence.
"""

PROMPT4_IMG = """
Create a festive yet minimal Instagram post for a jewellery brand using the uploaded product image.
Incorporate warm tones like gold, amber, or maroon with soft glowing highlights to evoke a subtle celebratory mood.
Use light festive accents like blurred florals, silk fabric, or candlelight — without clutter or bright contrasts.
Lighting should feel warm and elegant, giving the jewellery a radiant, handcrafted charm.
The final post should feel festive, royal, and timeless — ideal for festival campaigns.
"""

PROMPT5_IMG = """
Design a modern brand identity Instagram post using the uploaded jewellery image.
Use elegant textured backgrounds and a harmonious color palette aligned with a luxury jewellery brand.
Keep the layout clean and balanced, leaving subtle negative space where brand logo or tagline could be added.
Lighting should highlight the jewellery softly while maintaining brand consistency and visual harmony.
The output should look cohesive, sophisticated, and editorial — ideal for brand storytelling posts.
"""
