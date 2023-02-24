import pyautogui
import webbrowser
from time import sleep

# INICIALIZAÇÃO
pyautogui.alert(text='INICIALIZANDO BOT, POR FAVOR NÃO MEXER NA MAQUINA', title='waning')


sleep(0.8)
webbrowser.open('https://www.instagram.com/')
sleep(1)

# area imgs
entrar = pyautogui.locateCenterOnScreen('entrar.png')
salvar = pyautogui.locateCenterOnScreen('salvar.png')
pesquisar = pyautogui.locateCenterOnScreen('pesquisar.png')

# LOGIN
pyautogui.click(851,277, duration=0.8)
user = pyautogui.prompt(text='Telefone, nome de usuário ou email', title='bot-login')
passw = pyautogui.password(text='Senha', title='bot-login', mask='*')
sleep(0.3)
pyautogui.typewrite(user, interval=0.1)
pyautogui.press('tab')
pyautogui.typewrite(passw, interval=0.1)
sleep(0.5)
pyautogui.press('enter')
sleep(5)

# ENCONTRAR PERFIL
pyautogui.click(814,517, duration=0.5)
sleep(0.6)
pyautogui.click(37,252, duration=0.8)
sleep(0.8)
pesquisar_user = pyautogui.prompt(text='Nome do usuário', title='searcher')
sleep(0.3)
pyautogui.typewrite(pesquisar_user, interval=0.1)
sleep(0.5)
pyautogui.move(180, 0, duration=0.5)
sleep(0.5)
pyautogui.click()
sleep(0.5)
pyautogui.move(400, 0, duration=0.8)
pyautogui.scroll(-400)
sleep(0.5)
pyautogui.click(478,375, duration=0.5)

# CURTIR FOTO

def voltar():
    pyautogui.click(1349,97, duration=0.6)
    sleep(0.5)
    pyautogui.click(84, 123, duration=0.6)
    sleep(60)

coracao = pyautogui.locateCenterOnScreen('coracao.png')

if coracao is not None:
    voltar()
elif coracao == None:
    pyautogui.click(745,710, duration=0.5)
    sleep(0.8)
    voltar()
else:
    print('erro')