import pika, json

from products.models import Product
from django.conf import settings

def products_event_listener():

    params = pika.URLParameters(settings.RABBITMQ_URL)

    connection = pika.BlockingConnection(params)

    channel = connection.channel()

    def product_create_callback(ch, method, properties, body):
        try:
            Product.objects.create(json.load(body.decode()))
            print('Product created successfully')
        except Exception as ex:
            print(ex)
        
    channel.basic_consume(queue='product-create', on_message_callback=product_create_callback)

    channel.start_consuming()



