from django.db import models
from custom_user.models import User



TYPE_CHOICES = (
    ('free','free'),
    ('paid', 'paid'),
)




# Create your models here.
class QuizCategory(models.Model):
    title = models.CharField(max_length=50)
    heading = models.CharField(max_length=150, null=True)
    type = models.CharField(max_length=500, blank=True, null=True, choices=TYPE_CHOICES, default='paid')
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    

class QuizQuestion(models.Model):
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    question = models.TextField()
    opt_1 = models.CharField(max_length=500)
    opt_2 = models.CharField(max_length=500)
    opt_3 = models.CharField(max_length=500)
    opt_4 = models.CharField(max_length=500)
    opt_5 = models.CharField(max_length=500, blank=True, null=True)
    opt_6 = models.CharField(max_length=500, blank=True, null=True)
    opt_7 = models.CharField(max_length=500, blank=True, null=True)
    right_opt = models.CharField(max_length=500)
    questionimage = models.ImageField(upload_to ='questionimages/', blank=True, null=True)
    

    class Meta:
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question
    

class UserSubmittedAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    right_answer = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'User Submitted Answers'


class MyResults(models.Model):
    subject = models.CharField(max_length=50)
    percentage = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'My Results'


class Progress(models.Model):
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    percentage = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'My Progress'



class Payment(models.Model):
    phoneno = models.CharField(max_length=10, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Payment'

# Create your models here.
