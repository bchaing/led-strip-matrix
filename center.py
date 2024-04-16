import board
import neopixel
import time
pixels = neopixel.NeoPixel(board.D18, 256)

try:
	while True:
		pixels[119] = (255,255,255)
		time.sleep(1)
		pixels.fill((0,0,0))
		pixels[120] = (255,255,255)
		time.sleep(1)
		pixels.fill((0,0,0))
		pixels[135] = (255,255,255)
		time.sleep(1)
		pixels.fill((0,0,0))
		pixels[136] = (255,255,255)
		time.sleep(1)
		pixels.fill((0,0,0))
except:
	pixels.fill((0,0,0))
	pass
