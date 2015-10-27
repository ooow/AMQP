#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='Queue311_Goga')
str = raw_input("What to send ? ")
channel.basic_publish(exchange='',
                      routing_key='Queue311_Goga',
                      body= str)
print " [x] Sent str"
connection.close()