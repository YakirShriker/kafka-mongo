from kafka import KafkaConsumer
import requests
import json
from time import sleep
import logging
logging.basicConfig(level=logging.INFO)


def kafka_connector(boostrap_server):
    consumer_def = KafkaConsumer('sample',bootstrap_servers=boostrap_server,
                                 group_id ='group1',
                                 auto_offset_reset='latest')
    return consumer_def


def send_api_server(data):
    response = requests.post('http://apiserver:5100/buyrequest/', json=data)
    return response.text


def data_send():
    message = consumer.poll(timeout_ms=500)
    if message:
        for key, value in message.items():
            for record in value:
                insert = json.loads(record.value)
                insert['timestamp'] = record.timestamp
                response_from_api = send_api_server(insert)
                return response_from_api


if __name__ == '__main__':
    consumer = kafka_connector('kafka:9092')
    while True:
        res = data_send()
        if res:
            consumer.commit()
        else:
            sleep(5)
