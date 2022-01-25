"""IMPORTAR ARQUIVO PAPT DO SINACOR"""
from msvcrt import open_osfhandle
import os
from turtle import position
import dotenv
import pyautogui as p


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

def open_import():
    p.click(217,300)
    #p.hotkey("down")
    #p.hotkey("down")
    #p.hotkey("down")
    p.sleep(4)

def open_location_file():
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

def open_file():
    p.sleep(10)   
    p.click(629,390)
    p.hotkey("down")
    p.hotkey("down")
    p.hotkey("down")
    p.hotkey("down")
    p.press("enter")
    p.sleep(1)
    p.click(825,442)

kill_sina()
open_sina()
open_modulos()
open_import()
open_location_file()
open_file()



