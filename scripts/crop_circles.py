import os
from PIL import Image, ImageDraw

input_dir = "recursos"
output_dir = "book/_static/team"
os.makedirs(output_dir, exist_ok=True)

images = [
    ("alvaro.png", "alvaro.png"),
    ("andre.jpg", "andre.png"),
    ("daniel.jpg", "daniel.png"),
    ("diego.jpg", "diego.png"),
    ("hector.jpg", "hector.png"),
    ("juan.jpg", "juan.png"),
    ("sergio perez.jpg", "sergio_perez.png"),
    ("sergio.jpg", "sergio_garcia.png")
]

for in_name, out_name in images:
    in_path = os.path.join(input_dir, in_name)
    out_path = os.path.join(output_dir, out_name)
    
    if not os.path.exists(in_path):
        print(f"Skipping {in_name}, not found.")
        continue
        
    try:
        img = Image.open(in_path).convert("RGBA")
        
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
        
        # Resize to standard size for consistency
        output = output.resize((150, 150), Image.Resampling.LANCZOS)
        
        output.save(out_path, format="PNG")
        print(f"Cropped and saved {out_path}")
    except Exception as e:
        print(f"Error processing {in_name}: {e}")

