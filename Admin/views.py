from django.shortcuts import render,redirect
from django.contrib import messages
from datetime import datetime
from Admin.models import Contact,Service,Feature,Social_Links,Card,Team,Portfolio
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
obj = Social_Links.objects.all()
data = { 'link' : obj }

def home(request):
    servicedata = Service.objects.all()
    feature  = Feature.objects.all()
    link = Social_Links.objects.all()
    data = { 'data':servicedata,
            'data2': feature,
            'link':link 
            }
    return render(request,'index.html',data)


def about(request):
    return render(request,'about.html',data)

def service(request):
    service = Service.objects.all()
    card = Card.objects.all()
    data['service'] = service 
    data['card'] = card
    return render(request,'service.html',data)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        desc = request.POST.get('message')
        data3 = Contact(name=name,email=email,subject=subject,phone=phone,desc=desc,date=datetime.today())
        data3.save()

        # mail
        subject = 'PixalBreeze - Your Form Has Submitted'
        message = f'''Hello {name} ,
Welcome To Pixal Breeze IT Services,I hope Your are Fine !

    recently,You Visit Our site PixalBreeze And send Your opinion with this details :
        1. Name : {name}
        2. Email : {email}
        3. Contact No. : {phone}
        4. subject : {subject}
        5. Message : {desc}

    Thanks For Feedback ! Our Customer expert send you Replay mail Very Soon and Answer Your Message very Short time !

Thanks For Visit PixalBreeze !
        '''
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail( subject, message, email_from, recipient_list )

        messages.success(request,"Form Has Been Submitted !!!")
        
    return render(request,'contact.html',data)

def portfolio(request):
    portfolio = Portfolio.objects.all()
    data['portfolio'] = portfolio
    return render(request,'portfolio.html',data)

def team(request):
    team = Team.objects.all()
    data['team'] = team
    return render(request,'team.html',data)
