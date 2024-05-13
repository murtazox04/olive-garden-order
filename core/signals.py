import json
from django.dispatch import receiver
from django.forms import model_to_dict
from django.db.models.signals import post_save
from payme.models import MerchantTransactionsModel

from config.producer import producer
from .models import Order


@receiver(post_save, sender=MerchantTransactionsModel)
def produce_payment_successfully(sender, instance, created, **kwargs):
    if instance.state == 2:
        print("----------------------------------------")
        order = Order.objects.get(pk=instance.order_id)
        data = model_to_dict(order)
        data['amount'] = instance.amount
        json_data = json.dumps(data)
        producer.produce('main_topic', key='main_topic', value=json_data)

        producer.flush()
        print("----------------------------------------")
