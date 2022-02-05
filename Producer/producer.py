from flask import Flask, request, render_template
from kafka import KafkaProducer
import json
import requests
import logging
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)


def kafka_connector(boostrap_server):
    producer_def = KafkaProducer(bootstrap_servers=boostrap_server,
                                 retries=5,
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    return producer_def


def kafka_send_topic(producer, topic_name, message_json):
    producer.send(topic_name, message_json)
    producer.flush(timeout=10)
    producer.close(timeout=5)


@app.route('/', methods=["GET", "POST"])
def buy_request():
    if request.method == "POST":
        topicname = 'sample'
        bootstrap_server = ['kafka:9092']
        username = request.form.get("username")
        userid = request.form.get("userid")
        price = request.form.get("price")
        data = {'username': username,
                'userid': userid,
                'price': price}
        kafka_send_topic(kafka_connector(bootstrap_server), topicname, data)
    return render_template("index.html")


@app.route('/query', methods=["GET", "POST"])
def query():
    if request.method == "POST":
        userid = request.form.get("userid")
        res = requests.get('http://apiserver:5100/query/{0}'.format(userid))
        return res.text


@app.route('/queryall', methods=["GET", "POST"])
def query_all():
    if request.method == "POST":
        res = requests.get('http://apiserver:5100/query')
        return res.text


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
