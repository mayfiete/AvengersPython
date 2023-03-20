

import pika
import json
from DbConnx import DbConnx
import csv

# RabbitMQ connection parameters
# enhancement to have these in a config file or have calling application pass in
rabbitmq_host = 'localhost'
rabbitmq_port = 5672
rabbitmq_username = 'guest'
rabbitmq_password = 'guest'
rabbitmq_exchange = 'data_exchange'
rabbitmq_queue = 'data_queue'

# PostgreSQL connection parameters
conn = DbConnx()
conn.connect()


# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=rabbitmq_host,
    port=rabbitmq_port,
    credentials=pika.PlainCredentials(rabbitmq_username, rabbitmq_password)
))

channel = connection.channel()

# Declare the exchange and queue
channel.exchange_declare(exchange=rabbitmq_exchange,
                         exchange_type='direct', durable=True)
channel.queue_declare(queue=rabbitmq_queue, durable=True)
channel.queue_bind(exchange=rabbitmq_exchange,
                   queue=rabbitmq_queue, routing_key=rabbitmq_queue)


# connect to postgres
connection_postgresql = conn.conn


# Define the callback function to handle incoming messages


def callback(ch, method, properties, body):
    data = json.loads(body)
    # Insert the data into the database
    conn.execute(
        "INSERT INTO character_comic (name, comic) VALUES (%s, %s) ON CONFLICT DO NOTHING;")
    connection_postgresql.commit()
    print(f"Data inserted into database: {data}")


# Start consuming messages
channel.basic_consume(queue=rabbitmq_queue,
                      on_message_callback=callback, auto_ack=True)

print('Waiting for messages...')
channel.start_consuming()

# Close the connections
channel.close()
connection.close()
connection_postgresql.close()
