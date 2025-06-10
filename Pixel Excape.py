from microbit import *
import random

ship_x = random.randint(2, 4)
score = 0

while True:
    enemy_x = random.randint(0, 4)

    for y in range(5):
        display.clear()
        display.set_pixel(ship_x, 4, 9)
        display.set_pixel(enemy_x, y, 9)

        if button_a.was_pressed() and ship_x > 0:
            ship_x -= 1
        if button_b.was_pressed() and ship_x < 4:
            ship_x += 1

        sleep(70)

        if y == 4:
            if enemy_x == ship_x:
                display.scroll("Score: {}".format(score))
                sleep(2000)
                reset()
            else:
                score += 1
                if score == 30:
                    display.scroll("CLEAR!")
                    while True:
                        pass
