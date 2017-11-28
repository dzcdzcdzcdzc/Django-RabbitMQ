#!/usr/bin/env python
import pika

host = 'localhost'
queue = 'task_queue'


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
    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
channel = connection.channel()
channel.queue_declare(queue=queue, durable=True)  # durable queue声明为持久化
channel.basic_qos(prefetch_count=1)  # 再同一时刻，不要发送超过1条消息给一个worker，直到它已经处理了上一条消息并且作出了响应
channel.basic_consume(callback, queue=queue)
channel.start_consuming()
