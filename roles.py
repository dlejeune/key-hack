import keyboard
from time import sleep

sleep(4)

commands = [
    "Cows",
    "!emojify Hello",
    "Memes"
]

for command in commands:
    keyboard.write(command)
    keyboard.send('enter')
    sleep(1)
    pass
