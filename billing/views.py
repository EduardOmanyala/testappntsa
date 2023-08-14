from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django_daraja.mpesa.core import MpesaClient
from django.views.decorators.csrf import csrf_exempt
import json
from billing.models import StatusPayment, ContactDetails, Post #, PaymentConfirm
from django.db.models import Max
from django.contrib.auth.decorators import login_required
from core.forms import ContactsForm
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


@csrf_exempt
def callbackurl(request):
    if request.method == 'POST':
        m_body =request.body.decode('utf-8')
        mpesa_payment = json.loads(m_body)
        payment = StatusPayment(
            phoneno=mpesa_payment['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value'],
        	transcode=mpesa_payment['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value'],
        )
        payment.save()
        context = {
             "ResultCode": 0,
             "ResultDesc": "Accepted"
        }
        return JsonResponse(dict(context))
    



    
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
class ContactsAddView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = ContactsForm()
        context = {'form':form}
        return render(request, 'billing/paymentcontacts.html', context)
    
    def post(self, request, *args, **kwargs):
           
        form = ContactsForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return HttpResponse('form saved successfully')
        

class GeeksUpdateView(LoginRequiredMixin, UpdateView):
    model = ContactDetails
    fields = ["number"]
    #template_name_suffix = "billing/paymentcontacts.html"
    


# listings/views.py

@login_required
def band_update(request, id):
    #user = request.user
    band = ContactDetails.objects.get(id=id)
    form = ContactsForm(instance=band) # prepopulate the form with an existing band
    return render(request, 'billing/paymentcontacts.html', {'form': form})
  
 
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
    mydata = Post.objects.filter(user=request.user)
    if not mydata:
        return redirect('post-create')
    else:
        blogs = Post.objects.filter(user=request.user).values_list('pk', flat=True)
        numpk = blogs[0]
        return render(request, 'billing/paydetailsconfirm.html', {'mydata':mydata, 'numpk':numpk})
    
@login_required
def paydetailsmpesa(request):
    return render(request, 'billing/paydetailsmpesa.html')



@login_required
def finalizepay(request):
    userphones = Post.objects.filter(user=request.user).values_list('phonenumber', flat=True)
    userphone = userphones[0]
    updateduserphone = userphone[1:]
    first = '254'
    finalphoneno = first + updateduserphone
    finalstuff = eval(finalphoneno)
    qs = list(StatusPayment.objects.values_list('phoneno'))
    for phoneno in qs:
        print(phoneno)
        print(finalstuff)
        #print(finalphoneno)
        if phoneno == finalstuff:
            return HttpResponse('Payment received successfully!')
        else:
            return HttpResponse('they are NOT the samejnjj!')


