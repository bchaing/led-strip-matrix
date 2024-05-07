from led_matrix import *

matrix = LEDMatrix(16,16,board.D18)

for i in range(8):
    for j in range(16):
        matrix.set_pixel(15-i,15-j,(255,255,255))
        matrix.set_pixel(i,j,(255,255,255))
        matrix.show()
