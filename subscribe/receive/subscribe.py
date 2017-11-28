#!/usr/bin/env python
import pika
import time

host = 'localhost'
exchange = 'logs'


def callback(ch, method, properties, body):
    """
    消费方法
    :param ch:
    :param method:
    :param properties:
    :param body:
    :return:
    """
    print(body)


connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
channel = connection.channel()
channel.exchange_declare(exchange=exchange, exchange_type='fanout')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange=exchange, queue=queue_name)
channel.basic_consume(callback, queue=queue_name, no_ack=True)
channel.start_consuming()
