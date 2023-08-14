from django.urls import path
from billing import views
from billing.views import ContactsAddView, PostCreateView, PostDetailView, PostUpdateView

urlpatterns = [
    path('mpesa/request', views.mpesarequest, name='mpesastkrequest'),
    path('makeapayment', views.makeapayment, name='make-a-payment'),
    path('checkpayment', views.finpayment, name='fin-pay'),
    path('finalizepayment', views.paydetailsmpesa, name='paymentroute'),
    #path('finalizepay', views.finalizepay, name='finish-pay'),
    path('pricing/standard', views.pricing_standard, name='pricing-standard'),
    path('pricing/institutes', views.pricing_corporate, name='pricing-institutes'),
    path('pricing', views.pricing, name='pricing'),
    path('callback', views.callbackurl, name='callback'),
    path('paymentnumber', ContactsAddView.as_view() ),
    #path('paymentupdate/<int:pk>/', GeeksUpdateView.as_view() ),
    #path('contacts/<int:pk>/update/', ContactsUpdateView.as_view(), name='post-update'),
    #path('<pk>/contactsupdate/', views.band_update, name='contactsupdate'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
]