'''Bot de curtidas e comentários no Instagram com PyautoGUI.'''

import webbrowser
import pyautogui
from time import sleep

def logout():
    pyautogui.click(1324,129,duration=1)
    pyautogui.click(1288,687,duration=2)
    pyautogui.click(956,231,duration=1)
    pyautogui.click(1037,555,duration=1)
    
while True:
    # 1 - Navegar até o site https://www.instagram.com/
    webbrowser.open_new_tab('https://www.instagram.com/')
    sleep(5)
    # 2 - Entrar com meu usuário
    pyautogui.click(974,318,duration=1)
    pyautogui.typewrite('jordeilsonlima9@gmail.com')
    # 3 - Entrar com a minha senha
    pyautogui.hotkey('tab')
    pyautogui.typewrite('9902604310Jo@')
    pyautogui.click(1009,401,duration=1)
    sleep(5)
    # 4 - Clicar em "log in"
    pyautogui.click(1030,538,duration=1)
    sleep(4)

    # 5 - Pesquisar pela página
    pyautogui.click(1102,142,duration=1)
    pyautogui.typewrite('nike')
    sleep(3)
    # 6 - Entrar na página
    pyautogui.click(1128,214,duration=1)
    sleep(3)
    pyautogui.scroll(-500)
    # 7 - Clicar na postagem mais recente
    pyautogui.click(818,327,duration=1)
    # 8 - Verificar se já curtiu ou não aquela postagem
    coração = pyautogui.locateCenterOnScreen('coracao.png')
    sleep(2)

    if coracao is not None:
        logout()
        sleep(86400)
    elif coracao == None:
        pyautogui.click(936,572,duration=2)
        sleep(5)
        pyautogui.click(983,570,duration=2)
        pyautogui.click(1006,656,duration=1)
        pyautogui.typewrite('Gostei dessa foto.')
        sleep(2)
        pyautogui.click(1195,659,duration=1)
        logout()
        sleep(86400)
    






    







