#!/usr/bin/env python

import pika

host = 'localhost'
queue = 'hello'


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
channel.queue_declare(queue=queue)
channel.basic_consume(callback, queue=queue, no_ack=True)
channel.start_consuming()
