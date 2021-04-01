from Prediction import *

from flask import Flask, request

app = Flask(__name__)

@app.route("/result",methods = ['POST'])
def result():
    extract_json = request.get_json(silent=True,force=True)

    """
    quotes in a list
    """
    quotes  = extract_json.get("quotes")

    pred = predict(quotes)

    return pred

if __name__ == '__main__':
    app.run()
