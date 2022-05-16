from flask import Flask, render_template , request
import argparse

from config import config

app = Flask(__name__)



@app.route('/', methods = ['POST','GET'])
def registro():
    return render_template('/registro.html')

@app.route('/api',methods = ['POST','GET'])
def api():
    out= request.form.to_dict()
    return render_template('/API.html')

@app.route('/encuesta', methods = ['POST','GET'])
def encuesta():
    return render_template('/encuesta.html')

@app.route('/res', methods = ['POST','GET'])
def res():
    out1= request.form.to_dict()
    return render_template('/res.html')

@app.route('/recomiendame', methods = ['POST','GET'])
def recomiendame():
    return render_template('/recomiendame.html')

@app.route('/calificame', methods = ['POST','GET'])
def calificame():
    return render_template('/calificame.html')




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="expose")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    opt = parser.parse_args()
    app.config.from_object(config['development'])
    app.run(host="0.0.0.0", port=opt.port)