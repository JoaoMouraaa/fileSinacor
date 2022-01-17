
"""IMPORTAR ARQUIVO PAPT DO SINACOR"""
import os
import dotenv
import pyautogui as p


# carrega os valores dos arquivos
dotenv.load_dotenv(dotenv.find_dotenv())

user_name = os.getenv("user_name")
password = os.getenv("password")

os.startfile('C:/Sinacor HML/BMFBOVESPA/SinacorHML/UI/Application/Sinacor.exe')
p.sleep(5)

p.write(user_name)
p.hotkey('tab')
p.write(password)
#posicao login x=685, y=367
#posicao senha x=708, y=391
p.sleep(4)
#(x=679, y=419)
p.click(679,419)
# posicao = p.position()
# print(posicao)

print("User:", user_name)
print("Senha:", password)