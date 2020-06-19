#Recibe:
#Hora Inicio
#Hora final
#Intervalos (Necesito funcion que sume tiempos)
#Lugar
horai= str(request.form['horai'])#Aqui tomaría la hora inicial
fecha= str(request.form['fecha'])#fecha inicial
fechafin=str(request.form['fecha']) #Fecha fin xd
limite= str(request.form['limite'])#hora final
intervalo=int(request.form['intervalo'])#tiempo xd
lugar= str(request.form['lugar'])#Lugar xd
validas=[]
invalidas=[]
while fecha<=fechafin:
    hora_i=horai
    while hora_i<limite and hora_i<="23:59" and hora_i>=hora_inicio_jornada:
        horaf=sumtime(horai,intervalo) #Esta funcion esta en otro .py
        if horario_valido(medic,fecha,hora_i,horaf) :
            nomape=personal_medico[medic][0]+" "+personal_medico[medic][1]
            datoscita={"fecha":fecha,"hora_final":horaf,"hora_inicial":hora_i,"lugar":lugar,"medico":nomape,"especialidad":personal_medico[medic][4],"paciente":None}
            validas.append(datoscita)
            citas_medicos[medic].append(datoscita)
        else:
            invalidas.append(datoscita)
        hora_i=horaf
    fecha=sumadia(fecha,1)

p1=[] #Hay que crear una "base" y una "tapa"
for x in invalidas:
    p1.append(render_template('').format()) #Crear base, tabla que diga error, sla cita no ha sido creada pues su horario no es válido
p2=[] #Hay que crear una "base" y una "tapa"
for x in validas:
    p2.append(render_template('').format())
p1="".join(p1)
p2="".join(p2)
return render_template('',medic=medic).format(p1,p2) #Template que en {0} tiene a los datos erroneos bien ordenados y en {1} los datos validos ordenados
#Crear 3 templates, uno completo y dos complemetarios