from led_matrix import *
from time import sleep
import board

NUM_ROWS = 16
NUM_COLS = 16

LED_PIN = board.D18

matrix = LEDMatrix(NUM_ROWS, NUM_COLS, LED_PIN)

# RED
matrix.fill((255,0,0))
matrix.show()
sleep(1)

# Green
matrix.fill((0,255,0))
matrix.show()
sleep(1)

# Blue
matrix.fill((0,0,255))
matrix.show()
sleep(1)

# White
matrix.fill((255,255,255))
matrix.show()
sleep(1)

matrix.clear(show=True)

# 1 by 1
# Horizontal
for x in range(16):
    for y in range(16):
        matrix.clear()
        matrix.set_pixel(x,y,(255,255,255))
        matrix.show()

# Vertical
for y in range(16):
        for x in range(16):
            matrix.clear()
            matrix.set_pixel(x,y,(255,255,255))
            matrix.show()

matrix.clear(show=True)
