from django.http import HttpResponse
from rabbitmq.rabbitmq import RabbitMQ

mq = RabbitMQ()
chan = mq.get_mq_channel()
queue = 'delay'


# Create your views here.
def delay(request):
    chan.exchange_declare(exchange='dlx.' + queue, exchange_type='topic')
    chan.queue_declare(queue=queue, arguments={'x-dead-letter-exchange': 'dlx.' + queue})
    if request.method == 'GET':
        chan.basic_publish(exchange='', routing_key=queue, body='Hello World!',
                           properties=mq.basic_properties(
                               expiration='60000',  # 过期时间毫秒
                           ))
    else:
        chan.basic_publish(exchange='', routing_key=queue, body=request.body,
                           properties=mq.basic_properties(
                               expiration='60000',  # 过期时间毫秒
                           ))
    return HttpResponse()
