@app.route('/miscitas<cc>')
def mis_citas(cc):
    mc=["""<container ><table border WIDTH="990" ><tr><th>Especialidad</th><th>Fecha</th> <th>Hora</th><th>Médico</th><td></td> </tr>"""]
    if citas_paciente[cc]!=[]
        for i in range(len(citas_paciente[cc])):
            time=citas_paciente[cc][i]["hora_inicial"]+"-"+citas_paciente[cc][i]["hora_final"]
            citas.append(render_template('tablacitas2.html', cc=cc).format(citas_paciente[cc][i]["especialidad"],citas_paciente[cc][i]["fecha"],time,citas_paciente[cc][i][i]["medico"],citas_paciente[cc][i]["codigo"]))
        mc.append("</table></container>")
        mc="".join(mc)
    else:
        mc="<h1>No tienes citas programadas</h1>"
    return render_template('miscitas.html', cc=cc).format(mc)