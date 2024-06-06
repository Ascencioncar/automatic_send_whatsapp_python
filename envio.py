import pandas as pd
import pyautogui as pg
import webbrowser as web
import time 

data= pd.read_excel("/home/administrador/Descargas/proyecto envio/proyecto envio de wpp/informacion.xlsx")
print(data)

for i in range(len(data)):
    # dato a leer
    celular= data.loc[i,"Cel"].astype(str) #convierte en string
    nombre= data.loc[i,"Nombre"]
    estudioR= data.loc[i,"Estudio realizado"]
    
    mensaje="Hola, "+ nombre + " Te hiciste "+ estudioR +" Con nosotros, nos gustaría saber tu experiencia "
    
    chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
    web.open("https://web.whatsapp.com/send?phone="+celular+"&text="+mensaje)
    
    time.sleep(35)
    pg.click(812,768)
    time.sleep(4)
    pg.press("enter")
    
    time.sleep(3.5)
    #pg.hotkey("ctrl","w")
    time.sleep(1)
    