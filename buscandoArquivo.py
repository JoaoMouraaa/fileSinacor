"""
Bucando Arquivo e Data
"""

from datetime import datetime, timedelta
import os
import time


src = "C:\Estudos (Python)\ArquivoB3"
data_atual = datetime.now() - timedelta(days=3)

today = str(data_atual.strftime('%d/%m/%Y')) 
print(today)
  
for raiz, diretorios, arquivos in os.walk(src):
    for file in arquivos:        
        date_file = time.strftime("%d/%m/%Y", time.gmtime(os.path.getctime(src + "\\" + file)))
        #print(date_file, file)

        if date_file == today:
            print(file, date_file)

