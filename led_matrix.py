import board
import neopixel
import random

class LEDMatrix:
    def __init__(self, num_rows, num_cols, led_pin):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.led_pin = led_pin
        self.pixels = neopixel.NeoPixel(self.led_pin, self.num_rows * self.num_cols, auto_write=False)

    def get_index(self, row, col):
        if row % 2 == 0:
            return (row + 1) * self.num_cols - col - 1
        else:
            return row * self.num_cols + col

    def set_pixel(self, row, col, color):
        index = self.get_index(row, col)
        self.pixels[index] = color

    def show(self):
        self.pixels.show()

    def clear(self, show=False):
        self.pixels.fill((0, 0, 0))
        if show:
            self.pixels.show()

    def fill(self, color):
        self.pixels.fill(color)

    def image(self, image, resample=None):
        width, height = image.size
        if width != self.num_cols or height != self.num_rows:
            image = image.resize((self.num_rows, self.num_cols), resample=resample)

        image.convert("RGB")
        pixel_data = (image.getpixel((x, y)) for y in range(height) for x in range(width))

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                pixel_color = next(pixel_data)
                self.set_pixel(row, col, pixel_color)

def rand_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))
