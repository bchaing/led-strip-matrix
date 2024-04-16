from led_matrix import *
from PIL import Image, ImageDraw, ImageFont
from time import sleep 

TEXT_COLOR = (255,255,255)
BG_COLOR = (0,0,0)

matrix = LEDMatrix(16,16,board.D18)

font = ImageFont.load_default(12)
text = "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG. the quick brown fox jumped over the lazy dog."
text_width = int(font.getlength(text))

canvas = Image.new("RGB", (text_width + 16, 16), BG_COLOR)
draw = ImageDraw.Draw(canvas)
draw.text((16, 0), text, font=font, fill=TEXT_COLOR)

viewport_x = 0

# Pre-render frames
frames = []
while viewport_x <= canvas.width:
    cropped_text = canvas.crop((viewport_x, 0, viewport_x + 16, 16))
    frames.append(cropped_text)
    viewport_x += 1

# Display frames
for f in frames:
    matrix.image(f)
    matrix.show()
