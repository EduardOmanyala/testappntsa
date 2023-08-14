from django.db import models
from custom_user.models import User
from django.urls import reverse

# Create your models here.
class StatusPayment(models.Model):
    phoneno = models.TextField()
    transcode = models.TextField()
    class Meta:
        verbose_name = 'Status Payment'
        verbose_name_plural = 'Status Payments'
    def __str__(self):
        return self.phoneno
    

class ContactDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Contact Detail'
        verbose_name_plural = 'Contact Details'

    def __str__(self):
        return self.number



class Post(models.Model):
    phonenumber = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.phonenumber

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class PaymentConfirm(models.Model):
    evaluate = models.CharField(max_length=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Payment Confirmation'
        verbose_name_plural = 'Payment Confirmations'
    def __str__(self):
        return self.evaluate
    
