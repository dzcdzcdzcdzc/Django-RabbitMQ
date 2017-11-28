import pika


class RabbitMQ:
    mq_host = 'localhost'
    __mq_connection = None
    __mq_channel = None

    def get_mq_connection(self):
        if not self.__mq_connection:
            self.__mq_connection = pika.BlockingConnection(
                pika.ConnectionParameters(self.mq_host, heartbeat=0))
        return self.__mq_connection

    def get_mq_channel(self):
        if not self.__mq_channel:
            self.__mq_channel = self.get_mq_connection().channel()
        return self.__mq_channel

    @staticmethod
    def basic_properties(**option):
        return pika.BasicProperties(**option)

    def __del__(self):
        if self.__mq_channel:
            self.__mq_channel.close()
        if self.__mq_connection:
            self.__mq_connection.close()
