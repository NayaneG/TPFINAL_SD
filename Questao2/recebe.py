__author__ = "Jean Nunes"
__copyright__ = "Copyright 2018"
__credits__ = ["Jean Nunes"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Jean Nunes"
__email__ = "jean.to@gmail.com"
__status__ = "Development"
__app__ = "RabbitMQ"
__examples__ = "https://www.rabbitmq.com/getstarted.html"

import pika
import os

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='nip', exchange_type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='nip', queue=queue_name)

print(' [*] Aguardando logs. [ CTRL+C ] para sair ')

def callback(ch, method, properties, body):
    file_name = "nip_receive" + str(os.getpid()) + ".log"
    with open(file_name, "w+") as arquivo:
        print("{}\n".format(body), file=arquivo)
        print(" [x] log recebido e salvo no arquivo: %r" % file_name)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()