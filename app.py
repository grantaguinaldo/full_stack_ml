from flask import Flask, jsonify, request, render_template
from sklearn.linear_model import LogisticRegression
from joblib import load
import numpy as np

app = Flask(__name__)


@app.route('/is_alive')
def api_alive():
    return 'I am alive!'


@app.route('/')
def main_page():
    return render_template('index.html')


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

    y_pred_class_dict = dict(zip(['iris_class'], y_pred_class))

    y_pred_proba = pkl_lr.predict_proba(input_array).tolist()

    y_pred_class_prob_dict = dict(zip(['iris_class_prob'], y_pred_proba))

    # Dict Unpacking: https://www.python.org/dev/peps/pep-0448/
    y_pred_package = {**y_pred_class_dict, **y_pred_class_prob_dict}

    return jsonify(y_pred_package)


if __name__ == '__main__':
    app.run(debug=True)
