from django.http import HttpResponse
from rabbitmq.rabbitmq import RabbitMQ
import json

mq = RabbitMQ()
chan = mq.get_mq_channel()
exchange = 'direct_logs'


# Create your views here.
def routing(request):
    chan.exchange_declare(exchange=exchange, exchange_type='direct')
    if request.method == 'GET':
        chan.basic_publish(exchange=exchange, routing_key='error', body='Hello World!')
    else:
        body = json.loads(request.body)
        chan.basic_publish(exchange=exchange, routing_key=body['routing'], body=body['body'])
    return HttpResponse()
