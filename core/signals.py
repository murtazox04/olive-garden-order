from django.dispatch import receiver
from django.db.models.signals import post_save
from payme.models import MerchantTransactionsModel


@receiver(post_save, sender=MerchantTransactionsModel)
def produce_payment_successfully(sender, instance, created, **kwargs):
    if instance.state == 2:
        pass
