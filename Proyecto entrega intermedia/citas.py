@app.route('/citasdisponibles<cc>')
def vercitas(cc):
    base=[]
    citas=["""<container ><table border WIDTH="990" ><tr><th>Especialidad</th><th>Fecha</th> <th>Hora</th><th>Médico</th><td></td> </tr>"""]
    for x in personal_medico:
        if citas_medicos[x]!=[]:
            for i in citas_medicos[x]:
                if i["paciente"]==None:
                    time=i["hora_inicial"]+"-"+i["hora_final"]
                    f=x+i
                    citas.append(render_template('tablacitas.html', f=f)).format(i["especialidad"],i["fecha"],time,i["medico"])
    if citas=["""<container ><table border WIDTH="990" ><tr><th>Especialidad</th><th>Fecha</th> <th>Hora</th><th>Médico</th><td></td> </tr>"""]:
        t="<h1>No hay citas disponibles</h1>"
    else:
        citas.append("</table></container>")
        t="".join(citas)
    return render_template('citasdisponibles.html',cc=cc).format(t)
                    
