import board
import neopixel
import time
pixels = neopixel.NeoPixel(board.D18, 256)

try:
    while True:
        for x in range(0,256):
            pixels[x] = (255,255,255)

            if x == 0:
                pixels[255] = (0,0,0)
            else:
                pixels[x-1] = (0,0,0)
        for y in range(0,256):
            pixels[255-y] = (255,255,255)
            if not y == 0:
                pixels[256-y] = (0,0,0)
except:
    pixels.fill((0,0,0))
