#!/usr/bin/env python3

from flask import Flask, jsonify, request
import logging
import pymongo
import encoder
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)


@app.route('/query', methods=['GET'])
def query_all():
    purchases = mongo.ironsource_shop.purchase
    output = []
    for buy in purchases.find():
        output.append(buy)
    return jsonify({'result' : output})


@app.route('/query/<userid>', methods=['GET'])
def query_user_id(userid):
    purchases = mongo.ironsource_shop.purchase

    query = purchases.find({'userid' : userid})
    output = []
    for buy in query:
        output.append(buy)
    return jsonify({'result' : output})


@app.route('/buyrequest/', methods=['POST'])
def add_buy():
    purchases = mongo.ironsource_shop.purchase
    message = request.json
    userid = message['userid']
    purchases.insert_one(message)
    new_framework = purchases.find({'userid' : userid})
    output = []
    for q in new_framework:
        output.append(q)
    return jsonify({'result' : output})


if __name__ == '__main__':
    mongo = pymongo.MongoClient("mongodb://mongorootuser:yakir123@mongodb_container:27017/")
    app.json_encoder = encoder.MyEncoder
    app.run(host='0.0.0.0', debug=True, port=5100)