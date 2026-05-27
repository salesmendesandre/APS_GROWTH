import os
from PIL import Image, ImageDraw

input_path = "recursos/yolanda.jpeg"
output_path = "book/_static/team/yolanda.png"

try:
    img = Image.open(input_path).convert("RGBA")
    
    # Make square
    min_dim = min(img.size)
    left = (img.size[0] - min_dim) / 2
    top = (img.size[1] - min_dim) / 2
    right = (img.size[0] + min_dim) / 2
    bottom = (img.size[1] + min_dim) / 2
    img = img.crop((left, top, right, bottom))
    
    # Create mask
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + img.size, fill=255)
    
    # Apply mask
    output = Image.new('RGBA', img.size, (0, 0, 0, 0))
    output.paste(img, (0, 0), mask)
    
    # Resize to standard size
    output = output.resize((150, 150), Image.Resampling.LANCZOS)
    
    output.save(output_path, format="PNG")
    print(f"Cropped and saved {output_path}")
except Exception as e:
    print(f"Error processing {input_path}: {e}")
