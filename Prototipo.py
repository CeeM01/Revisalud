from flask import Flask, request, render_template,redirect,url_for #Se importan las liberias de flask   
import datetime  #Esta libreria funciona para manejar el tema de fechas
from datetime import date
app = Flask(__name__) #Aqui se crea la variable sobre la que estarán el resto de rutas 
datos_personales={} #Aquí se almacenarán las cc como llaves y una lista de los datos personales como valores
historia_clinica={} #Aquí irá como llaves las cc y como valores una listas o diccionarios o diccionarios anidados, no recuerdo gg con los datos personales,obvio
contraseñas={"admin":"1234"} #Aqui estarían almacenadas las contraseñas de los usuarios, también la del admin
personal_medico={"12345":"prueba"} #Aquí irían los datos de cada médico, que el admin agregaría, pero de momento, lo tengo así para no complicarme registrando un médico cada vez que quiero probar algo
contra_medicos={"12345":"12345"} #Aquí iria la contraseña de los médicos funcionando de forma literalmente identica a la de los users
def edad_usuario(datos_personales,cc): #Ya que la edad del usuario no será una variable fija, esta función determina la edad a partir de la fecha de nacimiento en formato aaaa-mm-dd
    fecha_de_nacimiento=str(datos_personales[cc][4])  
    x=fecha_de_nacimiento.split("-")
    ano_a=int(datetime.datetime.now().strftime("%Y"))
    mes_a=int(datetime.datetime.now().strftime("%m"))
    dia_a=int(datetime.datetime.now().strftime("%d"))
    dia=int(x[2])
    mes=int(x[1])
    ano=int(x[0])
    a=ano_a-ano
    m=mes_a-mes
    d=dia_a-dia
    if m>=0:
        if m==0:
            if d>=0:
                return a
            else:
                return int(a-1)
        else:
            return int(a)
    else:
        return int(a-1)
@app.route('/') # En la ruta "/" estará la pagina inicial 
def home():
    return render_template('home.html') #Aqui se importa el html de home
@app.route('/registro')
def registro():
    return render_template('registro1.html')  #Aqui el usuario verifica sus datos para configurar su contraseña
@app.route('/log_in') #Aqui el user se debe loggear
def log_in():
    return render_template('login.html')
@app.route('/log_inmedic')
def log_inmedic():  #Login pero del personal medico
    return render_template('loginmedic.html')
@app.route('/logginmedic') #Luego del loggeo de los medicos, puede suceder 3 casos *más el caso de que sea el admin
def loggin2():
    medico=request.args['username']
    contraseña=request.args['password']
    if medico=="admin" and contraseña=="1234":
        return home_admin() #si es el admin, retornará el home de admin
    else:
        if medico in personal_medico:
            if contraseña==contra_medicos[medico]:
                return redirect(url_for('home_medic',medic=medico)) #Contraseña correcta, todo ok, redirige a homemedic
            else:
                return render_template('contraseñaincorrecta.html') #Contraseña incorrecta **Hacer una para medicos
        else:
            return render_template('usuarionoregistradologin.html').format(medico)  #Personal no registrado, no está en el diccionario contra_medicos **hacer pa medicos
@app.route('/home_user<cc>') 
def home_user(cc):
    a=datos_personales[cc][0]+" "+datos_personales[cc][1]  #a es nombres+apellidos, para el saludo inicial :v
    notas_medicas=[] #Aqui se agregaran las notas medicas (consultas, ya convertidas a tabla, para luego unirlas)
    if historia_clinica[cc]["consultas"]==[]: #Si no se han hecho notas medicas...
        nm="NO ESPECIFICA" #imprimira no especifica
    else:
        nm=['"<container ><table border WIDTH="990" ><tr><th colspan="3">Notas médicas</th>"'] #Esta sería como la cabeza de la tabla
        for x in historia_clinica[cc]["consultas"]: #Cada consulta...
            nm.append(render_template('tabla.html').format(x["fecha"],"nombre ejemplo","especialidad ej",x["motivo"],x["revision"],x["examen"],x["diagnostico"],x["tratamiento"]))    #Usa la plantilla html de las tablas, remplazando los valores por los de la nota **
        nm.append("</table></container>") #Cierre de la tabla
        nm="".join(nm) #Une las sub tablas, por llamarlas de alguna forma
    return render_template('homeuser.html').format(a,cc,datos_personales[cc][3],datos_personales[cc][4],edad_usuario(datos_personales,cc),datos_personales[cc][5],datos_personales[cc][6],datos_personales[cc][7],historia_clinica[cc]["peso"],historia_clinica[cc]["altura"],nm) #Retorna el home en la que están los datos personales y las notas médicas
@app.route('/loggin') #Aqui se viene despues de el loggin de usuario, con las 3 posibilidades
def loggin():
    cc=request.args['username']
    contraseña=request.args['password']
    if cc=="admin" and contraseña=="1234":
        return home_admin()
    else:
        if cc in datos_personales:
            if contraseña==contraseñas[cc]:
                return redirect(url_for('home_user',cc=cc)) #todo ok
            else:
                return render_template('contraseñaincorrecta.html')  #...
        else:
                return render_template('usuarionoregistradologin.html').format(cc) #No está registrado
@app.route('/home_medic<medic>')
def home_medic(medic):
    return render_template('homemedic.html') #... *De momento no tiene casi nada
@app.route('/añadir_nota_medica') #funcion a la que se accede desde homemedic
def agregar_nota_medica():
        return render_template('añadirnotamedica.html') #html en el que se solicitan los campos para la nota médica
@app.route('/notamedica',methods=["POST"])
def notamedica():
    cc=request.form['cedula'] #La cc del paciente a la que se quiere agregar la nota médica
    if cc in datos_personales: #Verifica que el usuario exista
        fecha=str(date.today())
      #  medico=request.form['medic']
        especialidad="especialidad" #escpecialidad xdxd
        motivo=request.form['motivo']
        revisionxsistemas=request.form['revision']
        examen=request.form['examen']
        diagnostico=request.form['diagnostico']
        tratamiento=request.form['tratamiento']
        notamedica={"fecha":fecha,"motivo":motivo,"revision":revisionxsistemas,"examen":examen,"diagnostico":diagnostico,"tratamiento":tratamiento} #,"medico":medico}
        historia_clinica[cc]["consultas"].append(notamedica)
        return render_template('pruebanotamedica.html').format(notamedica) #** Hay que pensar en que que poner, esto lo puse por probar solamente
    else:
            return render_template('usuarionoregistrado.html').format(cc) #Si el usuario no existe... gg **Reusé esta plantilla, hay que hacer una para que no retorne
    
    

@app.route('/admin')      
def home_admin():
    return render_template('admin.html') #Home Admin
@app.route('/validar_datos/validacion') #Aqui se validan los datos del registro
def validar_datos2():
        nombre=request.args['nombres'].strip().upper()
        apellidos=request.args['apellidos'].strip().upper()
        cc=request.args['cedula'].strip()
        sexo=request.args['sexo'].strip().upper()
        fecha_nacimiento=str(request.args['fecha_nacimiento'])
        edad=int(request.args['edad'].strip())
        if cc in contraseñas and cc in datos_personales:
            tupla=datos_personales[cc]
            if tupla[0]==nombre and tupla[1]==apellidos and tupla[3]==sexo and tupla[4]==fecha_nacimiento and edad==edad_usuario(datos_personales,cc): #Aquí se comparan los datos ingresados por el usuario con los del sistema (añadidos por el admin)
                return redirect(url_for("crear_contraseña", cc=cc)) #Si coinciden, permite crear contraseña **
            else:
                return render_template('datosincorrectos.html') #**
        else:
            return render_template('usuarionoregistrado.html').format(cc) #Si el usuario no ha sido registrado por el admin

    
@app.route('/crearcontraseña<cc>', methods=["POST","GET"])
def crear_contraseña(cc):
    if request.method=="POST":
        contraseña1=request.form['c1']
        contraseña2=request.form['c2']
        if contraseña1==contraseña2:
            contraseñas[cc]=contraseña1
            return render_template('contraseñacreada.html') 
        else:
            return render_template('contraseñasincongruentes.html')
    else:
        return render_template('crearcontraseña.html')

@app.route('/crear_usuario')
def crear_usuario():
    return render_template('crearusuario.html')
    
def ver_datos():
        nombre=request.args['nombres'].strip().upper()
        apellidos=request.args['apellidos'].strip().upper()
        cc=request.args['cc'].strip()
        sexo=request.args['sexo'].strip().upper()
        fecha_nacimiento=str(request.args['fecha_nacimiento'])
        telefono=request.args['telefono'].strip()
        ciudad_residencia=request.args['ciudad'].strip().upper()
        residencia=request.args['direccion'].strip().upper()
        if cc not in datos_personales:
            datos_personales[cc]=(nombre,apellidos,cc,sexo,fecha_nacimiento,telefono,ciudad_residencia,residencia)
            contraseñas[cc]=None
            historia_clinica[cc]={"peso":None,"altura":None,"antecedentes":None,"consultas":[]}
            return render_template('usuariocreadobien.html')
        else:
            return render_template('usuariorepetido.html').format(cc)
 #   except:
#        return render_template('usuariomalcreado.html') 
@app.route('/verificar_datos')
def verificar_datos():
    return ver_datos()

if __name__ == "__main__":
    app.run(debug=True)
 # Launch the FlaskPy dev server
 
