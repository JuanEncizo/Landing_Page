from flask import Flask, render_template
import argparse

from config import config

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/registro')
def registro():
    return render_template('/registro.html')

@app.route('/api')
def api():
    return render_template('/API.html')

@app.route('/encuesta')
def encuesta():
    return render_template('/encuesta.html')

@app.route('/feedback')
def feedback():
    return render_template('/feedback.html')

@app.route('/calificame')
def calificame():
    return render_template('/calificame.html')




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="expose")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    opt = parser.parse_args()
    app.config.from_object(config['development'])
    app.run(host="0.0.0.0", port=opt.port)