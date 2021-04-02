import time
import board
import touchio
import neopixel

touch_right = touchio.TouchIn(board.D6)
touch_left = touchio.TouchIn(board.D7)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixels.fill((0, 0, 0))

while True:
    print(touch_right.raw_value)
    if touch_left.value and touch_right.value:
        pixels.fill((0,0,0))
    elif touch_right.value:
        pixels.fill((255,0,0))
    elif touch_left.value:
        pixels.fill((70,0,0))
    time.sleep(.1)
