from django.db import models
from custom_user.models import User
from django.urls import reverse

# Create your models here.

    
# Create your models here.
class PaymentDetails(models.Model):
    phonenumber = models.TextField()
    transcode = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Payment Detail'
        verbose_name_plural = 'Payment Details'
    def __str__(self):
        return self.phonenumber
    



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
    
