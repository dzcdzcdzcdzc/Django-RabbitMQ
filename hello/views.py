from django.http import HttpResponse
from rabbitmq.rabbitmq import RabbitMQ

mq = RabbitMQ()
chan = mq.get_mq_channel()
queue = 'hello'


# Create your views here.
def hello(request):
    chan.queue_declare(queue=queue)
    if request.method == 'GET':
        chan.basic_publish(exchange='', routing_key=queue, body='Hello World!')
    else:
        chan.basic_publish(exchange='', routing_key=queue, body=request.body)
    return HttpResponse()
