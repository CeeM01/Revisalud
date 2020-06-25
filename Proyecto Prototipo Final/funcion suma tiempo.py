#Recibe hora 1 y hora 2, retorna suma
from datetime import datetime, timedelta
def sumatime(hora1,tiempo):
    hora1=hora1.split(":")
    h1=int(hora1[0])
    m1=int(hora1[1])
    m=m1+int(tiempo)
    mn=m%60
    hn=h1+(m//60)
    if mn<10:
        mn="0"+str(mn)
    if hn<10:
        hn="0"+str(hn)
    return str(hn)+":"+str(mn)
def sumadia(fecha,fact):
    fecha = datetime.strptime(fecha, "%Y-%m-%d")
    fecha+= timedelta(days=fact)
    return str(fecha).split()[0]

    

