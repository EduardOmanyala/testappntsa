from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django_daraja.mpesa.core import MpesaClient
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from billing.models import Post, PaymentDetails, Contact
from django.contrib import messages
#from django.db.models import Max
from django.contrib.auth.decorators import login_required
from custom_user.models import User

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# Create your views here.


def mpesarequest(request):
    cl = MpesaClient()
    phone_number = '0740408496'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

# Include user pk on callback( request, pk), then create new model record with user pk
@csrf_exempt
def callbackurl(request, id):
    user_id = User.objects.get(id=id)
    if request.method == 'POST':
        m_body =request.body.decode('utf-8')
        mpesa_payment = json.loads(m_body)
        payment = PaymentDetails(
            phonenumber=mpesa_payment['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value'],
        	transcode=mpesa_payment['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value'],
            user=user_id,
        )
        payment.save()
        context = {
             "ResultCode": 0,
             "ResultDesc": "Accepted"
        }
        return JsonResponse(dict(context))
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['phonenumber']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['phonenumber']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False
    
class PostDetailView(DetailView):
    model = Post



class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['phonenumber']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Contact
    fields = ['phonenumber']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False
    
class ContactDetailView(DetailView):
    model = Contact


@login_required
def makeapayment(request):
    return render(request, 'billing/makepayment.html')

def pricing(request):
    return render(request, 'billing/pricing.html')

@login_required
def pricing_standard(request):
    return render(request, 'billing/pricing_standard.html')

@login_required
def pricing_corporate(request):
    return render(request, 'billing/pricing_corporate.html')

@login_required
def finpayment(request):
    mydata = Post.objects.filter(user=request.user).order_by('-id')[:1]
    if not mydata:
        return redirect('post-create')
    else:
        blogs = Post.objects.filter(user=request.user).values_list('pk', flat=True)
        numpk = blogs[0]
        return render(request, 'billing/paydetailsconfirm.html', {'mydata':mydata, 'numpk':numpk})

@login_required
def yearlypayments(request):
    mydata = Contact.objects.filter(user=request.user).order_by('-id')[:1]
    if not mydata:
        return redirect('contact-create')
    else:
        blogs = Contact.objects.filter(user=request.user).values_list('pk', flat=True)
        numpk = blogs[0]
        return render(request, 'billing/yearlypaydetailsconfirm.html', {'mydata':mydata, 'numpk':numpk})
    
@login_required
def paydetailsmpesa(request):
    return render(request, 'billing/paydetailsmpesa.html')

@login_required
def yearlypaydetailsmpesa(request):
    return render(request, 'billing/yearlypaydetailsmpesa.html')

@login_required
def processingpaymentpage(request):
    paydata = PaymentDetails.objects.filter(user=request.user)
    if not paydata:
        return render(request, 'billing/processingpaymentpage.html')
    else:
        messages.success(request, f'Payment completed successfully!')
        return redirect('dashboard')
    






