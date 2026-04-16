from flask import Flask, jsonify

from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/ubicacion")

def ubicacion():

    return jsonify({

        "payload":"guyana francesa 🚩"

    })

    

@app.route("/cohete")

def cohete():

    return jsonify({

        "payload":"apollo 13 🚀"

    })

    

@app.route("/despegar")

def despegar():

    return jsonify({

        "payload":"💥💥💥🚀"

    })

    

@app.route("/espacio")

def espacio():

    return jsonify({

        "payload":"🌍.➡️.🚀.➡️.🪐"

    })