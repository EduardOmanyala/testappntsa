from django.db import models
from custom_user.models import User

# Create your models here.
class EmailVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    verification_status = models.CharField(max_length=150, null=True)

    class Meta:
        verbose_name_plural = 'Email Verification'

    def __str__(self):
        return self.verification_status
