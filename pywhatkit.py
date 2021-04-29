import pyautogui as auto
import pywhatkit
import time
import pandas as pd

cliente = pd.read_excel("Clientes.xlsx")
cliente['Telefone'] = pd.to_numeric(cliente['Telefone'])

for index, row in cliente.iterrows():
    h = int(time.strftime('%H', time.localtime()))
    m = int(time.strftime('%M', time.localtime()))
    m = m+1
    msg = "Olá " + row['Nome'] + "tudo bem com você?"
    pywhatkit.sendwhatmsg('+5538991801928', msg, h, m)
    auto.PAUSE = 5
    auto.moveTo(1350,15)
    auto.click()
    auto.moveTo(820,375)
    auto.click()
