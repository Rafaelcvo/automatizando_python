import pyautogui as auto
import time
# auto.alert("Iniciando envio de mensagens!")

auto.press('winleft')
auto.write('chrome')
auto.press('enter')
time.sleep(3)
auto.press('enter')
auto.sleep(2)
auto.moveTo(300,50)
auto.doubleClick()
auto.write("https://api.whatsapp.com/send?phone=5538991801928")
auto.press('enter')