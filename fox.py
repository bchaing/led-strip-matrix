import board
import neopixel
from random import randint
from time import sleep
pixels = neopixel.NeoPixel(board.D18, 256, auto_write=False)

def draw_fox():
	try:
		background = (randint(0,255),randint(0,255),randint(0,255))
		black = (0,0,0)
		white = (255,255,255)
		fox = (255,50,0)

		pixels.fill(background)

		bar_px = [0,31,32,63,64,95,96,127,128,159,160,191,192,223,224,255]
		for i in bar_px:
			pixels[i] = black

		black_px = [36,44,60,58,52,50,67,70,74,77,92,88,87,86,82,99,101,102,106,107,109,124,123,115,114,131,141,156,154,148,146,162,165,167,168,169,171,174,162,165,167,168,169,171,174,189,183,177,193,207,221,220,210,209,228,229,230,231,232,233,234,235,236]
		for x in black_px:
			pixels[x] = black

		fox_px = [69,75,90,89,85,84,103,104,105,122,121,120,119,118,117,116,132,133,134,135,136,137,138,139,140,155,153,152,151,150,149,147,163,164,166,170,172,173,188,187,186,185,181,180,179,178,194,195,196,197,203,204,205,206,219,211]
		for y in fox_px:
			pixels[y] = fox

		white_px = [59,51,68,76,91,83,100,108,184,182,198,199,200,201,202,218,217,216,215,214,213,212]
		for z in white_px:
			pixels[z] = white
		pixels.show()
	except:
		pixels.fill((0,0,0))
		pass

try:
	while True:
		draw_fox()
		sleep(0.1)
	#draw_fox()
except:
	pixels.fill((0,0,0))
	#pixels.show()
	pass
