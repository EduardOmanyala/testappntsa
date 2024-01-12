from django.urls import path
from usermanager import views as manage_views

urlpatterns = [
    path('verify_email/test', manage_views.verifyEmail, name='verifyemail'),
    path('verify_email/iLdxMr8pCW0p57u0/68yhz2uu/<int:id>/$2y$10$Oixfkm5gRoCjlmHRgDVB5Z0T2RQ/', manage_views.EmailVerificationComplete, name='emailVerificationComplete'),
    path('blank/404', manage_views.blank, name='blank_404'),

]