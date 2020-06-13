import keyboard
with open(input("File\n:")) as file:
    f = lambda w :(keyboard.write(w), keyboard.send("enter"))
    [f(x) for x in [y.split(" ") for y in file]]
