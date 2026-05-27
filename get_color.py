from PIL import Image
from collections import Counter

img = Image.open('book/_static/logo.png')
img = img.convert('RGBA')

colors = img.getcolors(maxcolors=100000)
# Filter out transparent and whiteish
filtered = []
for count, color in colors:
    r, g, b, a = color
    if a > 100 and not (r > 240 and g > 240 and b > 240) and not (r < 20 and g < 20 and b < 20):
        filtered.append((count, color))

filtered.sort(reverse=True)
for count, color in filtered[:5]:
    r, g, b, a = color
    print(f"#{r:02x}{g:02x}{b:02x} - count: {count}")

