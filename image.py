from led_matrix import *
from PIL import Image
import argparse 
import sys

NUM_ROWS = 16
NUM_COLS = 16
LED_PIN = board.D18

DEFAULT_PATH = "Images/fox.png"

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("path", nargs="?", default=DEFAULT_PATH, help="Path to the image")
parser.add_argument("-n", "--nearest", help="Enables nearest neighbor resampling",
                    action="store_true")
args = parser.parse_args()

# Open image or throw error if not found
try:
	image = Image.open(args.path)
	image = image.convert("RGB")
except FileNotFoundError:
	print("Error: File not found.")
	sys.exit(1)

# Set resampling algorithm
resampling = None
if args.nearest:
    resampling = Image.Resampling.NEAREST

# Set matrix pixels
matrix = LEDMatrix(NUM_ROWS, NUM_COLS, LED_PIN)
matrix.image(image, resampling)
matrix.show()
