from flask import Flask, request, redirect, url_for, flash, jsonify, render_template
import pickle
import joblib
import json
import numpy as np
import gzip
from flask_cors import CORS

# fp = gzip.open('baseline_model.pkl.gz', 'rb')
with gzip.open('sm_baseline_model.pkl.gz', 'rb') as fp:
    model = joblib.load(fp)


def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def index():
        return render_template('reco.html')

    @app.route('/api', methods=['POST'])
    def prediction():
        ailment = request.form['ailment']
        relief = request.form['relief']
        booboo = ailment + relief
        print(booboo)
        prediction = np.array2string(model.predict([booboo]))
        return jsonify(prediction)
    return app
