import time
import board
import touchio
import neopixel

touch_right = touchio.TouchIn(board.D6)
touch_left = touchio.TouchIn(board.D7)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=.3)
pixels.fill((0, 0, 0))

def wheel(pos):
    if pos < 0 or pos > 255:
        return (0,0,0)
    elif pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    else:
        pos -= 170
        return (pos*3,0,255-pos*3)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(1):
            rc_index = (i * 256 // 1) + j
            pixels[i] = wheel(rc_index & 255)
            print(rc_index)
        pixels.show()
        time.sleep(wait)


while True:
    print(touch_right.raw_value)
    if touch_left.value and touch_right.value:
        pixels.fill((0,0,0))
    else:
        rainbow_cycle(.01)
