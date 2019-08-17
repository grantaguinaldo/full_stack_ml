from flask import Flask, jsonify, request
from joblib import load
import numpy as np

app = Flask(__name__)


@app.route('/is_alive')
def api_alive():
    return 'I is alive!'


@app.route('/api', methods=['GET'])
def get_prediction():
    # TODO: NEED TO GET DATA FROM THE GET REQUEST AND PASS IT INTO THE MODEL.
    n = request.args.get('n')

    input_data = np.array([])

    pkl_lr = load('iris_class')
    y_pred_class = pkl_lr(input_data)

    return_package = {'iris_class': y_pred_class}
    return jsonify(return_package)


if __name__ == '__main__':
    app.run(debug=True)
