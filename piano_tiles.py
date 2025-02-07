import pyautogui
import keyboard
import win32con
import win32api
from time import sleep

pyautogui.click(1045,384,duration=1)
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('1')==False:
    if pyautogui.pixelMatchesColor(944,354,(0,0,0)):
        click(944,354)
    if pyautogui.pixelMatchesColor(1018,348,(0,0,0)):
        click(1018,348)
    if pyautogui.pixelMatchesColor(1075,345,(0,0,0)):
        click(1075,345)
    if pyautogui.pixelMatchesColor(1139,342,(0,0,0)):
        click(1139,342)
