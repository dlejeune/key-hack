import keyboard
from time import sleep


file  = input("File:")

sleep(2)

with open(file) as f:
    people = f.readlines()

    for person in people:
        keyboard.write("!kick @{}".format(person))
        keyboard.send('enter')
        sleep(2)
    keyboard.write("!dump -f %u -r @CRU 1 @CRU 2 @CRU 3 @CRU 4 @CRU 5 @CRU 6")
    keyboard.send('enter')