"""IMPORTAR ARQUIVO PAPT DO SINACOR"""
from datetime import datetime
from msvcrt import open_osfhandle
import os
from socket import if_indextoname
import sys
from turtle import position
import zlib
import dotenv
import pyautogui as p
import clipboard as c


# carrega os valores dos arquivos
dotenv.load_dotenv(dotenv.find_dotenv())

user_name = os.getenv("user_name")
password = os.getenv("password")


def kill_sina():
    os.system('taskkill /im Sinacor.exe -f')
    p.sleep(3)

"""Abrindo o SINACOR"""
def open_sina():
    os.startfile('C:/Sinacor HML/BMFBOVESPA/SinacorHML/UI/Application/Sinacor.exe')
    p.sleep(8)

    p.write(user_name)
    p.hotkey('tab')
    p.write(password)
    p.sleep(1)
    p.click(679,419)
    p.sleep(5)

def open_modulos():
    p.click(626,301)
    p.sleep(3)
    p.hotkey("right","down")
    p.hotkey("down","right","down","right")
    p.press("enter")
    p.sleep(8)

def import_BVBG028(): 
    p.sleep(6)
    p.hotkey( "down")
    p.rightClick()
    p.sleep(1)
    p.press("tab")
    p.press("enter")
    p.sleep(1)
    p.click(844,400)
    p.sleep(1)
    p.click(857,306)
    p.write('C:\\Users\\joao.moura_icon\\Downloads')
    p.press("enter")
    p.sleep(1)
    p.click(735,419)
    p.sleep(2)
    p.press("enter")
    p.sleep(1)
    p.click(840,438)
    p.sleep(7)
    p.click(1025,263)
    p.sleep(3)
    
def import_BVBG086():
    p.click(256,234)
    p.hotkey("down")
    p.hotkey("down")
    p.hotkey("down")
    p.hotkey("down")
    p.hotkey("down")
    p.rightClick()
    p.sleep(1)
    p.press("tab")
    p.sleep(1)
    p.press("enter")
    p.sleep(1)
    p.click(844,400)
    p.sleep(1)
    p.click(857,306)
    p.write('C:\\Users\\joao.moura_icon\\Downloads')
    p.press("enter")
    p.sleep(1)
    p.sleep(1)
    p.click(735,419)
    p.sleep(1)
    p.hotkey("down")
    p.hotkey("down")
    p.hotkey("down")
    p.sleep(1)
    p.press("enter")
    p.sleep(1)
    p.click(840,438)
    p.sleep(7)
    p.click(1025,263)
    p.sleep(5)

def valid_file():  
    DATE_NOW = datetime.now() 
    today = str(DATE_NOW.strftime('%d/%m/%Y'))
    p.click(256,234)
    p.sleep(3)
    p.rightClick(291,233)
    p.sleep(3)
    p.click(326,366)
    p.sleep(2)
    text = c.paste()
    texto = text.upper().split()
    # validar a coluna status se esta finalizado com sucesso e se a data final esta preenchida com a date de hoje
    hi = 'SUCESSO'
    if hi in texto[25] and today in texto[29]:
        open_location_file()
    else:
        p.sleep(10)
        valid_file()
  
def open_location_file():
    p.sleep(3)
    p.click(200,304)
    p.sleep(2)
    p.rightClick(286,305)
    p.sleep(1)
    p.press('tab')
    p.sleep(2)
    p.press('enter')
    p.sleep(2)
    p.click(819,406)
    p.sleep(2)
    p.click(564,297)
    p.sleep(1)
    p.write('\\\sinaprod-01\\bvmf\\transfer\\mft-clearing\\receber')
    p.press('enter')

def import_PAPT():
    p.sleep(10)   
    p.click(629,390)
    p.hotkey("down")
    p.hotkey("down")
    p.hotkey("down")
    p.hotkey("down")
    p.sleep(2)
    p.press("enter")
    p.sleep(1)
    p.click(825,442)
    p.sleep(5)
    p.click(1024,264)


kill_sina()
open_sina()
open_modulos()
import_BVBG028()
import_BVBG086()
valid_file()
import_PAPT()



