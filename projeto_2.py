# Entender os passos manuais para depois criar o código python.

# Verificar se há um botão com a cor correspondente dentro do círculo daquela cor.

import pyautogui
import keyboard
from time import sleep

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(950,582,(0,152,0)):
        pyautogui.press('a')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1058,581,(255,0,0)):
        pyautogui.press('s')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1143,586,(244,244,2)):
        pyautogui.press('j')
        sleep(0.05)

