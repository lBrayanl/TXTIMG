from flask import Flask, render_template, request, jsonify
from pytesseract import *
from langdetect import detect_langs
from PIL import ImageTk, Image
import os
import glob

def detectar_idiomas(texto):
    return detect_langs(texto)
    #idiomas = detect_langs(texto)
    #idiomas_ordenados = sorted(idiomas, key=lambda x: x.prob, reverse=True)
    #return [lang.lang for lang in idiomas_ordenados[:3]]

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        f = request.files['file']
        f.save('static/img/' + f.filename)
        return f.filename
    else:
        return render_template("home.html")

@app.route("/procesarImagen", methods=["POST"])
def procesarImagen():
    pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    imagen = request.files["imagen"]

    ruta_imagen = "static/img/hola.png"
    imagen.save(ruta_imagen)

    texto = pytesseract.image_to_string(Image.open(ruta_imagen))
    idiomas_detectados = detectar_idiomas(texto)

    ordenarIdiomas = []

    print(idiomas_detectados)

    for lang in idiomas_detectados:
        ordenarIdiomas.append(str(lang))

    return jsonify({
        "texto": texto,
        "idiomas_detectados": ordenarIdiomas
    })

@app.route('/about', strict_slashes=False)
def about():
    image_filenames = os.listdir('static/img')
    return render_template("about.html", image_filenames=image_filenames)

@app.route('/we', strict_slashes=False)
def we():
    return render_template("we.html")

if __name__ == '__main__':
    app.run(debug=True)
