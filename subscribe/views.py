from django.http import HttpResponse
from rabbitmq.rabbitmq import RabbitMQ

mq = RabbitMQ()
chan = mq.get_mq_channel()
exchange = 'logs'


# Create your views here.
def subscribe(request):
    chan.exchange_declare(exchange=exchange, exchange_type='fanout')
    if request.method == 'GET':
        chan.basic_publish(exchange=exchange, routing_key='', body='Hello World!')
    else:
        chan.basic_publish(exchange=exchange, routing_key='', body=request.body)
    return HttpResponse()
