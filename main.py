import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(2)

pyautogui.click(x=445, y=396)
pyautogui.write("testeautomatizado@gmail.com")
pyautogui.press("tab")
pyautogui.write("teste123")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)
pyautogui.press("enter")
