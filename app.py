from flask import Flask
import requests

app = Flask(__name__)


def leer_txt_desde_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return ""

def obtener_personas_filtradas(ulr):
    contenido = leer_txt_desde_url(ulr)
    lineas = contenido.strip().split("\n")

    encabezado = lineas[0].split("|")
    datos = lineas[1:]

    ids_validos = ("3", "4", "5", "7")
    personas_filtradas = []

    for linea in datos:
        campos = linea.split("|")
        if campos[0].startswith(ids_validos):
            personas_filtradas.append(campos)
    return encabezado, personas_filtradas




@app.route("/")
def home():
    URL_DATOS = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt"
    encabezado, personas = obtener_personas_filtradas(URL_DATOS)

    tabla_html = "<table border='1' cellpadding='5'>"
    tabla_html += "<tr>" + "".join([f"<th>{col}</th>" for col in encabezado]) + "</tr>"

    for persona in personas:
        tabla_html += "<tr>" + "".join([f"<td>{dato}</td>" for dato in persona]) + "</tr>"

    tabla_html += "</table>"

    return f"{tabla_html}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)