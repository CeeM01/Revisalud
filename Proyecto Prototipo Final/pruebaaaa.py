from datetime import date, time,datetime,timedelta
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
"""horai= input('horazi')#Aqui tomaría la hora inicial
fecha= input('fechai')
fechafin=input('fechafin') #Fecha fin xd
limite= input('horafin')#hora final
intervalo=int(input('intervalo'))#tiempo xd
lugar= input('lugar')#Lugar xd
while fecha<=fechafin:
    hora_i=horai
    while hora_i<limite and hora_i<="23:59" and hora_i>="00:00":
        horaf=sumatime(hora_i,intervalo) #Esta funcion esta en otro .py
        datoscita={"fecha":fecha,"hora_final":horaf,"hora_inicial":hora_i,"lugar":lugar,"paciente":None}
        print(datoscita)
        hora_i=horaf
    fecha=sumadia(fecha,1)"""
########
def capitalizar(x):
    x=x.strip().split()
    if len(x)==1:
        x="".join(x)
        return x.capitalize()
    else:
        for n in range(len(x)):
            if x[n].isalpha():
                x[n]=x[n].capitalize()
        x=" ".join(x)
        return x
