# Entender os passos manuais para depois criar o código python.

# Verificar se há um botão com a cor correspondente dentro do círculo daquela cor.

import pyautogui
import keyboard
from time import sleep
import win32api
import win32con

pyautogui.click(1078,313,duration=1)
pyautogui.press('a')
def a(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,152,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,152,0)

def s(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,255,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,255,0,0)

def j(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,244,244,2)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,244,244,2)

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(950,582,(0,152,0)):
        pyautogui.press('a'(a(950,582)))
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1058,581,(255,0,0)):
        pyautogui.press('s'(s(1058,581)))
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1143,586,(244,244,2)):
        pyautogui.press('j'(j(1143,586)))
        sleep(0.05)

