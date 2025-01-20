from PIL import Image, ImageDraw, ImageFont

# Input nickname
nickname = "Sean"

# Create a blank image
image = Image.new('RGBA', (250, 200), (255, 255, 255, 0))

# Initialize drawing context
draw = ImageDraw.Draw(image)

# Load a handwriting font (download a .ttf handwriting font)
font_path = "Caveat-VariableFont_wght.ttf"
font = ImageFont.truetype(font_path, size=108)

# Add the nickname text
draw.text((30, 30), nickname, fill=(0, 0, 0), font=font)

# Save the image
image.save("Sean.png")

print("Signature saved as 'Sean.png'")
