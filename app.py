from flask import Flask, jsonify, request
from sklearn.linear_model import LogisticRegression
from joblib import load
import numpy as np

app = Flask(__name__)


@app.route('/is_alive')
def api_alive():
    return 'I am alive!'


@app.route('/prediction', methods=['GET'])
def get_prediction():

    sepal_length = request.args.get('sepallen')
    sepal_width = request.args.get('sepalwid')
    petal_length = request.args.get('petallen')
    petal_width = request.args.get('petalwid')

    input_list = [float(sepal_length), float(sepal_width), float(petal_length), float(petal_width)]
    input_array = np.array(input_list).reshape(1, -1)

    pkl_lr = load('iris_class')
    y_pred_class = pkl_lr.predict(input_array).tolist()
    y_pred_proba = pkl_lr.predict_proba(input_array).tolist()

    # TODO: Need to figure out the datatype from y_pred_class and
    #      y_pred_proba.

    y_pred_package = dict(zip(['iris_class'], y_pred_class))

    #TODO: NEED TO CREATE A DICT FROM

    # y_pred_package = {'iris_class': y_pred_class[0]
    #'iris_class_0_proba': y_pred_proba[0][0],
    #'iris_class_1_proba': y_pred_proba[0][1],
    #'iris_class_2_proba': y_pred_proba[0][2],
    #}

    return jsonify(y_pred_package)


if __name__ == '__main__':
    app.run(debug=True)
