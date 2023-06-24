from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    if request.method == "POST":
        to = request.POST.get('toemail')
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        send_mail(subject,content,settings.EMAIL_HOST_USER,[to])
    return render(request, 'msgbox.html',{'title' : 'Send an email'})