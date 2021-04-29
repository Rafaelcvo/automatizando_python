import pyautogui as auto
import pywhatkit
import time
import pandas as pd
import emoji

cliente = pd.read_excel("Clientes.xlsx", engine='openpyxl')

for index, row in cliente.iterrows():
    row['Telefone'] ='+55' + str(row['Telefone'])
    h = int(time.strftime('%H', time.localtime()))
    m = int(time.strftime('%M', time.localtime()))
    m = m+1
    msg = "Olá " + row['Nome'] + " tudo bem com você? " + \
          "\nÉ possível inserir texto passando uma promoção." + \
          '\n' + emoji.emojize("Podemos inserir emojis :red_heart:") + "." + \
          '\n\n' + "Inserir links https://www.instagram.com/rafaelcvo/"

    pywhatkit.sendwhatmsg(row['Telefone'], msg, h, m)
    auto.PAUSE = 5
    auto.moveTo(1350,15)
    auto.click()
    auto.moveTo(820,375)
    auto.click()