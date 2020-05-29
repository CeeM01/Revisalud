@app.route('añadircita<medic>')
def añadir_citas(medic):
    return render_template('añadircita.html',medic=medic)
@app.route('/añadircitanice<medic>')
def añadir_citas2(medic):
    fecha=str(request.form['fecha'])
    horai=str(request.form['hora'])
    horaf=str(request.form['hora2'])
    lugar=request.form['lugar']
    nomape=personal_medico[medic][0]+" "+personal_medico[medic][1]
    datoscita={"fecha":fecha,"hora_final":horaf,"hora_inicial":horai,"lugar":lugar,"medico":nomape,"especialidad":personal_medico[medic][4]}
    citas_medicos[medic].append(datoscita)
    return render_template('pruebacita.html').format(datoscitas)