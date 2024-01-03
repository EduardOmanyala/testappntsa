from django.urls import path
from billing import views
from billing.views import PostCreateView, PostDetailView, PostUpdateView, ContactCreateView, ContactDetailView, ContactUpdateView

urlpatterns = [
    path('mpesa/request', views.mpesarequest, name='mpesastkrequest'),
    path('makeapayment', views.makeapayment, name='make-a-payment'),
    path('processingpayment', views.processingpaymentpage, name='processing-payment'),
    path('checkpayment', views.finpayment, name='fin-pay'),
    path('payments/annual', views.yearlypayments, name='yearly-pay'),
    path('finalizepayment/monthly', views.paydetailsmpesa, name='paymentroute'),
    path('finalizepayment/annual', views.yearlypaydetailsmpesa, name='annualpayments'),
    path('paymentsflutter', views.paymentflutter, name='payflutter'),
    path('continue/payment', views.proceedToGateway, name='proceedtogateway'),
    path('continue/payment/plan/two', views.proceedToGatewayannual, name='proceedtogatewayannual'),


   
    path('pricing/standard', views.pricing_standard, name='pricing-standard'),
    path('pricing/institutes', views.pricing_corporate, name='pricing-institutes'),
    path('pricing', views.pricing, name='pricing'),
    path('callback/<int:id>/', views.callbackurl, name='callback'),
    path('callbackflutter/<int:id>/', views.call_back_flutter, name='callbackflutter'),
   

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('contact/new/', ContactCreateView.as_view(), name='contact-create'),
    path('contact/<int:pk>/update/', ContactUpdateView.as_view(), name='contact-update'),

    path('payments/review', views.paymentsTracker, name='paytracker'),
    path('payments/delete/<int:id>/', views.paymentsDelete, name='paydelete'),



    
]