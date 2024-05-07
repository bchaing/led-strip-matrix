from led_matrix import *
from random import randint
import board
from time import sleep

matrix = LEDMatrix(16,16,board.D18)
for x in range(500):
	row = randint(0,15)
	col = randint(0,15)
	matrix.set_pixel(row, col, (255,255,255))

	if row > 0:
		matrix.set_pixel(row-1, col, (255,255,255))
	if row < 15:
		matrix.set_pixel(row+1, col, (255,255,255))
	if col > 0:
		matrix.set_pixel(row, col-1, (255,255,255))
	if col < 15:
		matrix.set_pixel(row, col+1, (255,255,255))

	matrix.pixels.show()
	matrix.clear()

matrix.clear(show=True)
