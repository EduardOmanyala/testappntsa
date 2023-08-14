from django.contrib import admin
from django.contrib import admin
from . import models





# Register your models here.
admin.site.register(models.QuizCategory)

class QuizQuestionAdmin(admin.ModelAdmin):
    list_display=['question']


admin.site.register(models.QuizQuestion, QuizQuestionAdmin)


class UserSubmittedAnswerAdmin(admin.ModelAdmin):
    list_display = ['id','question','user','right_answer']
admin.site.register(models.UserSubmittedAnswer, UserSubmittedAnswerAdmin)



class PaymentAdmin(admin.ModelAdmin):
    list_display=['phoneno']


admin.site.register(models.Payment, PaymentAdmin)

admin.site.register(models.MyResults)

admin.site.register(models.Progress)
