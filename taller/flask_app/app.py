from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import json

from config import API_URL, HEADERS

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'una-clave-secreta-taller13'


@app.route("/")
def inicio():
    return render_template("menu.html")


# ---------------------------------------------------------
# EDIFICIOS
# ---------------------------------------------------------

@app.route("/edificios")
def listar_edificios():
    """
        Consume el servicio web de Django para listar los Edificios.
    """
    r = requests.get(f"{API_URL}/edificios/", headers=HEADERS)
    edificios = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("edificios.html", edificios=edificios, numero=numero)


@app.route("/edificios/crear", methods=['GET', 'POST'])
def crear_edificio():
    """
        Formulario que envía un POST al servicio web de Django
        para crear un nuevo Edificio.
    """
    if request.method == 'POST':
        edificio_data = {
            'nombre': request.form['nombre'],
            'direccion': request.form['direccion'],
            'ciudad': request.form['ciudad'],
            'tipo': request.form['tipo'],
        }

        r = requests.post(f"{API_URL}/edificios/", json=edificio_data, headers=HEADERS)

        if r.status_code == 201:
            flash("Edificio creado exitosamente!", "success")
            return redirect(url_for('listar_edificios'))
        else:
            flash(f"Error al crear el edificio: {r.content}", "danger")

    return render_template("crear_edificio.html")


# ---------------------------------------------------------
# DEPARTAMENTOS
# ---------------------------------------------------------

@app.route("/departamentos")
def listar_departamentos():
    """
        Consume el servicio web de Django para listar los Departamentos.
        Por cada departamento resuelve el nombre del edificio al que pertenece.
    """
    r = requests.get(f"{API_URL}/departamentos/", headers=HEADERS)
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']

    departamentos = []
    for d in datos:
        departamentos.append({
            'nombre_propietario': d['nombre_propietario'],
            'costo': d['costo'],
            'numero_cuartos': d['numero_cuartos'],
            'edificio': obtener_nombre_edificio(d['edificio']),
        })

    return render_template("departamentos.html", departamentos=departamentos, numero=numero)


@app.route("/departamentos/crear", methods=['GET', 'POST'])
def crear_departamento():
    """
        Formulario que envía un POST al servicio web de Django
        para crear un nuevo Departamento. Primero obtiene la lista
        de edificios disponibles para el selector del formulario.
    """
    r_edificios = requests.get(f"{API_URL}/edificios/", headers=HEADERS)
    edificios_disponibles = json.loads(r_edificios.content)['results']

    if request.method == 'POST':
        departamento_data = {
            'nombre_propietario': request.form['nombre_propietario'],
            'costo': request.form['costo'],
            'numero_cuartos': request.form['numero_cuartos'],
            'edificio': request.form['edificio'],  # URL del edificio
        }

        r = requests.post(f"{API_URL}/departamentos/", json=departamento_data, headers=HEADERS)

        if r.status_code == 201:
            flash("Departamento creado exitosamente!", "success")
            return redirect(url_for('listar_departamentos'))
        else:
            flash(f"Error al crear el departamento: {r.content}", "danger")

    return render_template("crear_departamento.html", edificios=edificios_disponibles)


# ---------------------------------------------------------
# funciones ayuda
# ---------------------------------------------------------

def obtener_nombre_edificio(url):
    """
        Recibe la URL hyperlinked de un edificio (ej.
        http://localhost:8000/api/edificios/1/) y devuelve su nombre.
    """
    r = requests.get(url, headers=HEADERS)
    return json.loads(r.content)['nombre']


if __name__ == "__main__":
    app.run(debug=True)
