
import time
import pyautogui
import os
import datetime


def screenshot():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    #    name = int(round(time.time()*1000))
    name = round(time.time())
    valid_date = datetime.datetime.fromtimestamp(name).strftime('%d-%m-%Y_%H-%M')
    name = f'{script_directory}/{valid_date}.png'
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()


screenshot()