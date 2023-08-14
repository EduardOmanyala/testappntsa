from django.db.models.signals import post_save
from django.dispatch import receiver
from billing.models import StatusPayment, Post



@receiver(post_save, sender=StatusPayment, dispatch_uid="update payment details")
def update_stock(sender, instance, created, **kwargs):
    if created:
        payno = instance.phoneno
        print(payno)

        