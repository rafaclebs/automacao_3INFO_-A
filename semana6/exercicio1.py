'''fazer uma pesquisa no google 
clique no campo de pesquisa, após digite o 
texto 'como automatizar o whatsapp
após pressione a tecla enter' 
'''
import pyautogui


pyautogui.click(460,490)
pyautogui.write('como automatizar o whatsapp', interval=0.1)
pyautogui.press('enter')
pyautogui.moveTo(30,325, duration=.5)
pyautogui.dragTo(410,450, duration=.5)
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1050,500, duration=.5)
pyautogui.hotkey('ctrl', 'v')