import shutil
from flask import Flask, render_template , request
import argparse
import os
from werkzeug.utils import secure_filename
from app_detect import*
from shutil import rmtree

from config import config

listaReg_glob = ""
app = Flask(__name__)

uploads_dir = os.path.join(app.instance_path, 'uploads')
os.makedirs(uploads_dir, exist_ok=True)


@app.route('/', methods = ['POST','GET'])
def registro():
    return render_template('/registro.html')

@app.route('/api',methods = ['POST','GET'])
def api():
    #out= request.form.to_dict()
    #lista = [*out.values()]
   # nombreReg= lista[0]
   # listaReg_glob=nombreReg
   # print(listaReg_glob)
    return render_template('/API.html')

@app.route('/encuesta', methods = ['POST','GET'])
def encuesta():
    out= request.form.to_dict()
    return render_template('/encuesta.html')
 

@app.route('/res', methods = ['POST','GET'])
def res():
    #nombre=listaReg_glob
    #print(nombre)
   # out1= request.form.to_dict()
    return render_template('/res.html')

@app.route('/recomiendame', methods = ['POST','GET'])
def recomiendame():
    return render_template('/recomiendame.html')

@app.route('/calificame', methods = ['POST','GET'])
def calificame():
    return render_template('/calificame.html')

@app.route('/encuestaproc', methods = ['POST','GET'])
def encuestaproc():

    if not request.method == "POST":
        return
    imagen_a_detectar = request.files['imagen_a_detectar']
    imagen_a_detectar.save(os.path.join(uploads_dir, secure_filename(imagen_a_detectar.filename)))
    print(imagen_a_detectar)
    
    detec_son(os.path.join(uploads_dir, secure_filename(imagen_a_detectar.filename)))
    obj = secure_filename(imagen_a_detectar.filename)

    contenido = os.listdir('.\\runs\\detect\\exp')
    shutil.copy(".\\runs\\detect\\exp\\"+contenido[0], ".\\src\\static\\img\\foto_detectada.jpg")
    rmtree(".\\runs\\detect\\exp")
    print(obj)
    print(contenido)

    return obj
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="expose")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    opt = parser.parse_args()
    app.config.from_object(config['development'])
    app.run(host="0.0.0.0", port=opt.port)