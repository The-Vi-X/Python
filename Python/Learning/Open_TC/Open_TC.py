import pyautogui
import time
import pyperclip
import os


def open(path="C:\\Users\\akamu\\OneDrive\\Рабочий стол\\telnet.bat"):
    os.system(f'start "" "{path}"')
    time.sleep(4)

def move_and_click():
    pyautogui.moveTo(945,585)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)


def paste(password="G!875342472707oh"):
    pyperclip.copy(password)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)

def connect():
    pyautogui.moveTo(855, 780)
    pyautogui.click()
    time.sleep(2)

open()
move_and_click()
paste()
connect()
input("Press Enter to exit.")