from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from billing.models import PaymentConfirm, PaymentDetails, PaymentInfo
from . import models
from core.models import QuizCategory, MyResults, QuizQuestion, UserSubmittedAnswer, Progress


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'core/home.html')



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account Created for {email}, you can now login')
            html_template = 'core/successemail.html'
            html_message = render_to_string(html_template)
            subject = 'Welcome to Testapp!'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            message = EmailMessage(subject, html_message,
                                   email_from, recipient_list)
            message.content_subtype = 'html'
            message.send(fail_silently=True)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form':form})




def categories(request):
    catData = models.QuizCategory.objects.all()
    return render(request, 'core/all-category.html', {'data':catData})

@login_required
def free_category_questions(request, cat_id):
    #paydata = PaymentConfirm.objects.filter(user=request.user)
    #if not paydata:
        #return redirect('make-a-payment')
    #else:
    category = QuizCategory.objects.get(id=cat_id)
    question = QuizQuestion.objects.filter(category=category).order_by('id').first()
    return render(request, 'core/questionslist.html', {'question':question, 'category':category})


@login_required
def category_questions(request, cat_id):
    paydata = PaymentInfo.objects.filter(user=request.user)
    if not paydata:
        return redirect('make-a-payment')
    else:
        category = QuizCategory.objects.get(id=cat_id)
        question = QuizQuestion.objects.filter(category=category).order_by('id').first()
        return render(request, 'core/questionslist.html', {'question':question, 'category':category})

@login_required
def submit_answer(request, cat_id, quest_id):
    if request.method=='POST':
        category = QuizCategory.objects.get(id=cat_id)
        questions1 = QuizQuestion.objects.all()
        question = questions1.filter(category=category,id__gt=quest_id).exclude(id=quest_id).order_by('id').first()

        quest = QuizQuestion.objects.get(id=quest_id)
        user = request.user
        answer = request.POST['answer']
        UserSubmittedAnswer.objects.create(user=user, question=quest, right_answer=answer)
        if question:
            return render(request, 'core/questionslist.html', {'question':question, 'category':category})
        else:
            result = UserSubmittedAnswer.objects.filter(user=request.user)
           
            
            score = 0
            percentage = 0
            for row in result:
                if row.question.right_opt == row.right_answer:
                    score+=1
            percentage = (score*100)/result.count()
            subject = UserSubmittedAnswer.objects.filter(user=request.user).first()
            subjectcat = subject.question.category
            MyResults.objects.create(user=user, percentage=percentage, subject=subjectcat)
            Progress.objects.create(user=user, percentage=percentage, category=category)
            UserSubmittedAnswer.objects.filter(user=request.user).delete()
            return render(request, 'core/results.html', {'result':result, 'score':score, 'percentage':percentage}) 
    else:
        return HttpResponse('Method not allowed!!')
    
#@login_required
#def dashboaord(request):
    #freetest = QuizCategory.objects.filter(type='free')
    #data = QuizCategory.objects.all()
    #paydata = PaymentConfirm.objects.filter(user=request.user)
    #return render(request, 'core/dashboard.html', {'data':data, 'paydata':paydata, 'freetest':freetest})

@login_required
def myresults(request):
    myresults = MyResults.objects.filter(user=request.user).order_by('-id')[:70]
    return render(request, 'core/userscores.html', {'myresults':myresults})

@login_required
def profile(request):
    return render(request, 'core/profile.html')


@login_required
def dashboaord(request):
    paydata = PaymentInfo.objects.filter(user=request.user)
    test1 = MyResults.objects.filter(user=request.user, subject="Test One").order_by('-id')[:1]
    test2 = MyResults.objects.filter(user=request.user, subject="Test Two").order_by('-id')[:1]
    test3 = MyResults.objects.filter(user=request.user, subject="Test Three").order_by('-id')[:1]
    test4 = MyResults.objects.filter(user=request.user, subject="Test Four").order_by('-id')[:1]
    test5 = MyResults.objects.filter(user=request.user, subject="Test Five").order_by('-id')[:1]
    test6 = MyResults.objects.filter(user=request.user, subject="Test Six").order_by('-id')[:1]
    test7 = MyResults.objects.filter(user=request.user, subject="Test Seven").order_by('-id')[:1]
    test8 = MyResults.objects.filter(user=request.user, subject="Test Eight").order_by('-id')[:1]
    test9 = MyResults.objects.filter(user=request.user, subject="Test Nine").order_by('-id')[:1]
    test10 = MyResults.objects.filter(user=request.user, subject="Test Ten").order_by('-id')[:1]
    return render(request, 
                  'core/newdashboard.html',
                   {'paydata':paydata,
                    'test1':test1,
                    'test2':test2,
                    'test3':test3,
                    'test4':test4,
                    'test5':test5,
                    'test6':test6,
                    'test7':test7,
                    'test8':test8,
                    'test9':test9,
                    'test10':test10
                    })



def about(request):
    return render(request, 'core/about.html')

def contactus(request):
    return render(request, 'core/contactus.html')



