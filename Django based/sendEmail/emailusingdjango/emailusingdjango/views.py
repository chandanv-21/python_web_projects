from django.core.mail import send_mail
from django.conf import settings
from django.http.request import HttpRequest
from django.shortcuts import render

def index(request):
    if request.method=='POST':
  
        subject=request.POST['subject']
        message= request.POST['message']
        email_from= settings.EMAIL_HOST_USER
        recipient_list=['chandanvishwakarma21@gmail.com',]
        send_mail(subject,message, email_from, recipient_list, fail_silently=False)
        
    return render(request, 'emailForm.html')
