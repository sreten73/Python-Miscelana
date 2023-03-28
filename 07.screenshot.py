
import time
import pyautogui
import os


def screenshot():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    name = int(round(time.time()*1000))
    name = f'{script_directory}/{name}.png'
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()


screenshot()