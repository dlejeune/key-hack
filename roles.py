import keyboard
from time import sleep

# Give time to alt-tab into discord
sleep(2)

members = {
    'Boks': [
        "[Swifts] Annabelle D",
        "[Boks] Simon B",
        "[Boks] Thomas C",
        "[Boks] Timothy vZS",
        "[Boks] Laura O"],

    'Bats': [
        "[Boks] Nina S",
        "[Bats] Rachel C",
        "[Bats] Mackenzie"],

    'Swifts': [
        "[Goshawks] Ephraim R",
        "[Swifts] Matthew K-W",
        "[Swifts] Aiden M",
        "[Swifts] Ethan G",
        "[Swifts] Kristen M",
        "[Swifts] Annabelle D"],

    'Eagles': [
        "[Eagles] Rozanna C",
        "[Eagles] Holly R",
        "[Eagles] Emily M",
        "[Eagles] Joel F",
        "[Eagles] Oliver H",
        "[Eagles] Ryan C"],

    'Goshawks': [
        "[Goshawks] Alex M",
        "[Goshawks] Zoe B",
        "[Goshawks] Juliette M",
        "[Goshawks] Malaika K"],

    'Kestrels': [
        "[Kestrels] Luke F",
        "[Swifts] Jack C",
        "[Kestrels] Bianca D",
        "[Kestrels] Timothy B",
        "[Kestrels] James W",
        "[Kestrels] Juliet D"]
}

for patrol in members.keys():
    for member in members[patrol]:
        # Figure out the previous patrol of the scout
        secondBracket = member.find(']')
        prevPatrol = member[1:secondBracket]

        print("{}'s prievious patrol was {}'".format(member, prevPatrol))

        # If the scout has moved, execute code. Else don't
        if prevPatrol != patrol:

            # Remove this role from the scout
            keyboard.write('!role remove "{}" {} '.format(member, prevPatrol))
            keyboard.send('enter')
            sleep(0.5)

            # Add new role to the scout
            keyboard.write('!role add "{}" {} '.format(member, patrol))
            keyboard.send('enter')
            sleep(0.5)

            # Change the nickname of the scout
            newNick = member.replace(prevPatrol, patrol)
            keyboard.write('!setnick "{}" {}'.format(member, newNick))
            keyboard.send('enter')
            sleep(0.5)
