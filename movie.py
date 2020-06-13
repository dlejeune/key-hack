import keyboard
from time import sleep


file_path = input("Enter the file path:\n")
seperator = input('Enter the separator (newline is N): \n')
sleep(2)

with open(file_path, 'r') as script:

    for line in script:
        if seperator != 'N':
            for word in line.split(seperator):
                keyboard.write(word)
                keyboard.send('enter')
