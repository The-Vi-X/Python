import pyautogui
import time
import pyperclip
import os

time.sleep(5)
def click_1():
    pyautogui.moveTo(175,150)
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(2)

def write_1(name):
    pyperclip.copy("Обхід пк " + name)
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'v')
    
def click_2():
    pyautogui.moveTo(919,564)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(1)

def click_3():
    pyautogui.moveTo(516,680)
    pyautogui.click()
    time.sleep(1)

def click_4():
    pyautogui.moveTo(1464,910)
    pyautogui.doubleClick()
    pyautogui.doubleClick()
    pyautogui.doubleClick()
    time.sleep(1)

def click_write_5():
    pyautogui.moveTo(1000,797)
    pyautogui.click()
    pyperclip.copy("Bogdan Borzak - iTIM")
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.moveTo(612,830)
    pyautogui.click()
    time.sleep(1)

def click_f():
    pyautogui.moveTo(1279,966)
    pyautogui.click()
    time.sleep(1)

with open("C:\\Users\\akamu\\OneDrive\\Рабочий стол\\users.txt", "r", encoding="utf-8") as file:
        usernames = file.readlines()

    # Проходим по каждому имени пользователя
for username in usernames:
    if username:  # Проверяем, что строка не пустая
        click_1()
        write_1(username)
        click_2()
        click_3()
        click_4()
        click_write_5()
        click_f()

file.close()
    