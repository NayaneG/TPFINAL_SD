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
import sys
import subprocess

# Sistema Operacional
so_p = subprocess.Popen(["uname", "-a"], stdout=subprocess.PIPE)
so_out, err = so_p.communicate()

# Hardware
hard_p = subprocess.Popen(["lshw", "-short"], stdout=subprocess.PIPE)
hard_out, err = hard_p.communicate()

# Rede
rede_p = subprocess.Popen(["ifconfig", "-a"], stdout=subprocess.PIPE)
rede_out, err = rede_p.communicate()

with open("nip.log", "w+") as arquivo:
    print("{}\n".format(so_out), file=arquivo)
    print("{}\n".format(hard_out), file=arquivo)
    print("{}\n".format(rede_out), file=arquivo)

with open("nip.log") as arquivo:
    info = str(arquivo.readlines())

##### Publish/subscribe #####
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='nip', exchange_type='fanout')

channel.basic_publish(exchange='nip',
                      routing_key='',
                      body=info)

print(" [x] Enviando log... ")

connection.close()