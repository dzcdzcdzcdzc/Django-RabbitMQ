from django.http import HttpResponse
from rabbitmq.rabbitmq import RabbitMQ

mq = RabbitMQ()
chan = mq.get_mq_channel()
queue = 'task_queue'


# Create your views here.
def work(request):
    chan.queue_declare(queue=queue, durable=True)  # durable queue声明为持久化
    if request.method == 'GET':
        chan.basic_publish(exchange='', routing_key=queue, body='Hello World!',
                           properties=mq.basic_properties(
                               delivery_mode=2,  # delivery 1是消息非持久化 2是消息持久化
                           ))
    else:
        chan.basic_publish(exchange='', routing_key=queue, body=request.body,
                           properties=mq.basic_properties(
                               delivery_mode=2,  # delivery 1是消息非持久化 2是消息持久化
                           ))
    return HttpResponse()
