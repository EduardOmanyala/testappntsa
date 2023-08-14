from django.contrib import admin
from billing.models import StatusPayment, ContactDetails, Post, PaymentConfirm
# Register your models here.
admin.site.register(StatusPayment)
admin.site.register(ContactDetails)
admin.site.register(Post)
admin.site.register(PaymentConfirm)