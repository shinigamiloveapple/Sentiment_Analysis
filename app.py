from Ml_pred import *

from flask import Flask, Request

app = Flask(__name__)

@app.route("/result",methods = ['POST'])
def result():
    message = request.form['message']

    