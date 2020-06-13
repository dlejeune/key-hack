import keyboard
from datetime import datetime as dt
from time import sleep


def sendReminder(reminderDate, delay, name="Luke", meeting_name="rover meeting"):
    today = dt.now()
    time_to_date = reminderDate - today

    while not (time_to_date == 0):
        days, seconds = time_to_date.days, time_to_date.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        keyboard.write("{} you have a rover meeting in {} days, {} hours, {} minutes and {} seconds ".format(name, days, hours, minutes, seconds))
        keyboard.send('enter')

        sleep(delay)

        today = dt.now()
        time_to_date = reminderDate - today
        pass


if __name__ == '__main__':

    sendReminder(dt(2020, 5, 17, 15), 1)
