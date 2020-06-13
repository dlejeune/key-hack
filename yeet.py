import pyautogui
import random
from time import sleep

# print("Calibration: place your mouse at the top left corner of the canvas")
# sleep(2)
# top_x = pyautogui.position()[0]
# top_y = pyautogui.position()[1]
# print(top_x, top_y)
# print("Calibration: place your mouse at the bottom right corner of the canvas")
# sleep(2)
# bottom_x = pyautogui.position()[0]
# bottom_y = pyautogui.position()[1]
# print(bottom_x, bottom_y)

sleep(1)

top_x = 234
top_y = 145
bottom_x = 1174
bottom_y = 723

pyautogui.moveTo(700, 415)
pyautogui.mouseDown(button='left')

prev_x = 700
prev_y = 415

possible_increments = [1, 2, 43, 25, -6, -3, -8, -10, 100, 4, 3, 2, 20]


def random_increment():
    return random.randint(-100, 100)


for i in range(100):
    change_colour = random.randint(0, 2)

    if 1 <= change_colour <= 2:
        pyautogui.mouseUp(button='left')
        if change_colour == 1:
            pyautogui.press('0')
            pass
        elif change_colour == 2:
            pyautogui.press('9')
            pass
        pyautogui.mouseDown(button='left')
        pass

    new_x = prev_x + random_increment()
    new_y = prev_y + random_increment()

    while (not (top_x <= new_x <= bottom_x)) or (not (top_y <= new_y <= bottom_y)):
        new_x = prev_x + random_increment()
        new_y = prev_y + random_increment()
        pass
    prev_x = new_x
    prev_y = new_y

    pyautogui.moveTo(new_x, new_y)
