from django.contrib import admin
from billing.models import  Post, PaymentConfirm, PaymentDetails, Contact, PaymentInfo
# Register your models here.

admin.site.register(Post)
admin.site.register(PaymentConfirm)
admin.site.register(PaymentDetails)
admin.site.register(Contact)
admin.site.register(PaymentInfo)