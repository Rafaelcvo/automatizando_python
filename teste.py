import pyautogui as auto
import pywhatkit
import time

tel = ['+', '+']

for i in tel:
    h = int(time.strftime('%H', time.localtime()))
    m = int(time.strftime('%M', time.localtime()))
    m = m+1
    print(h,m)

    pywhatkit.sendwhatmsg(i,"This is a message!",h,m)
    auto.PAUSE = 5
    auto.moveTo(1350,15)
    auto.click()
    auto.moveTo(820,375)
    auto.click()
