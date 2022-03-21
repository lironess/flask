import os
from flask import jsonify, request

from app.calc import ArithmeticOperation, Calcutation


def home():
    return jsonify(dict(all_routes=[{
        'GET': ['/files'],
        'POST': ['/calc']
    }]))


def list_files():
    all_files = [os.path.join(root, file) for root,
                 directories, files in os.walk('.') for file in files]
    return jsonify(dict(files=all_files))


def calc():
    payload = request.get_json()
    calculation = Calcutation(
        firstNum=payload['firstNum'], secondNum=payload['secondNum'], operation=ArithmeticOperation(payload['operation']))
    return jsonify(result=calculation.calculate())
