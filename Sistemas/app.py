from flask import Flask, render_template, request, redirect, url_for
import pyodbc

app = Flask(__name__)

# Configuración de la cadena de conexión a SQL Server con autenticación de Windows
connection_string = "DRIVER={SQL Server};SERVER=EDGARASUS\\SQLEXPRESS02;DATABASE=Carrera;Trusted_Connection=yes"

# Ruta para mostrar el formulario y guardar datos en la base de datos
@app.route('/', methods=['GET', 'POST'])
def principal():
    if request.method == 'POST':
        carnet = request.form['carnet']
        nombre = request.form['nombre']
        email = request.form['email']
        edad = request.form['edad']
        facultad = request.form['facultad']
        semestre_genero = request.form['semestre']
        talla = request.form['Talla']
        texto_playera = request.form['Texto Playera']
        numero_corredor = request.form['Numero Corredor']

        try:
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()
            # Inserta los datos en la tabla correspondiente
            cursor.execute("INSERT INTO corredor2 (Carnet, NombreCompleto, CorreoElectronico, Edad, Facultad, SemestreGenero, Talla, TextoPlayera, NumeroCorredor) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
               (carnet, nombre, email, edad, facultad, semestre_genero, talla, texto_playera, numero_corredor))


            conn.commit()
            conn.close()
            return redirect(url_for('principal'))
       
        except Exception as e:
         return f"Error: {str(e)}"

    return render_template('pagina.html')

if __name__ == '__main__':
    app.run(debug=True)
