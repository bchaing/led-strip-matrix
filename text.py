from led_matrix import *
from PIL import Image, ImageDraw, ImageFont

TEXT_COLOR = (255,255,255)
BG_COLOR = (0,0,0)

matrix = LEDMatrix(16,16,board.D18)

font = ImageFont.load_default(size=12)
text = "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG. the quick brown fox jumped over the lazy dog."
text_width = int(font.getlength(text))

# Create single canvas with text
canvas = Image.new("RGB", (text_width + (16*2), 16), BG_COLOR)
draw = ImageDraw.Draw(canvas)
draw.text((16, 0), text, font=font, fill=TEXT_COLOR)

# Pre-render frames
frames = [canvas.crop((x, 0, x + 16, 16)) for x in range(canvas.width + 16)]

# Display frames
for frame in frames:
    matrix.image(frame)
    matrix.show()
