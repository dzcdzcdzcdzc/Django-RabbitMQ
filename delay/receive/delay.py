#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='dlx.delay', exchange_type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='dlx.delay', queue=queue_name, routing_key='#')


def callback(ch, method, properties, body):
    print(method.routing_key, body, )


channel.basic_consume(callback, queue=queue_name, no_ack=True)
channel.start_consuming()
