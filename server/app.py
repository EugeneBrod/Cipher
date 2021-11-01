from flask import Flask, jsonify, request
from flask_cors import CORS
from Engine import Engine
from Beyond12 import Beyond12
from Parser import Parser
import numpy as np


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

app.config['CORS_HEADERS'] = 'Content-Type'


# server data
def setupServer():
    row1 = list("1234567890".upper())
    row2 = list("qwertyuiop".upper())
    row3 = list("asdfghjkl;".upper())
    row4 = list("zxcvbnm,./".upper())
    keyboard = np.array([row1, row2, row3, row4])
    transformer = Beyond12()
    parser = transformer.generateParser()
    engine = Engine(keyboard, transformer)
    return engine, parser

engine, parser = setupServer()
TLIST = parser.getListFromString("")


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong dudes!')

@app.route('/keyboard', methods=['GET'])
def transformKeyboard():
    response_object = {'status': 'success', 'finished': False}
    if (not TLIST):
        response_object["finished"] = True
        return jsonify(response_object)
    transformation = TLIST.pop(0)
    engine.transformArray(transformation)
    engine.translateString()
    response_object['string'] = engine.getOriginalString()
    response_object['transformedString'] = engine.getTransformedString()
    response_object['indicies'] = engine.getIndicies()
    result = engine.getTransformedArray()
    flattened_list = [j for sub in result for j in sub]
    response_object['numColumns'] = len(result[0])
    response_object['array'] = flattened_list
    response_object['transformationsString'] = engine.getTransformationString()
    return jsonify(response_object)

@app.route('/reset', methods=['POST'])
def reset():
    response_object = {'status': 'success'}
    engine.reset()
    TLIST[:] = parser.getListFromString("")
    return jsonify(response_object)

@app.route('/dump', methods=['GET'])
def dump():
    response_object = {'status': 'success'}
    response_object['string'] = engine.getOriginalString()
    response_object['transformedString'] = engine.getTransformedString()
    response_object['indicies'] = engine.getIndicies()
    result = engine.getTransformedArray()
    flattened_list = [j for sub in result for j in sub]
    response_object['numColumns'] = len(result[0])
    response_object['array'] = flattened_list
    response_object['transformationsString'] = engine.getTransformationString()
    return jsonify(response_object)

@app.route('/setStrings', methods=['PUT'])
def setStrings():
    response_object = {'status': 'success', 'finished': False}
    post_data = request.get_json()
    reset()
    engine.setString(post_data['string'])
    engine.translateString()
    lst = parser.getListFromString(post_data['transformationString'])
    for l in lst:
        TLIST.append(l)
    response_object['string'] = engine.getOriginalString()
    response_object['transformedString'] = engine.getTransformedString()
    response_object['indicies'] = engine.getIndicies()
    result = engine.getTransformedArray()
    flattened_list = [j for sub in result for j in sub]
    response_object['numColumns'] = len(result[0])
    response_object['array'] = flattened_list
    response_object['transformationsString'] = engine.getTransformationString()
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
