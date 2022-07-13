import pika

def product_create(params, message): # ik, not the best use-case, but i wasnt really able to come up with any better, that wouldn't be an overkill
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.basic_publish(exchange='', routing_key='product-create', body=message)
    channel.close()
    
