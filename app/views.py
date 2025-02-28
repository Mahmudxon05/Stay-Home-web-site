from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index_view(request):
    home = Home.objects.first()
    ourservis = OurServices.objects.last()
    context = {
        'home' : home,
        'our': ourservis,
        'services': ServicesTypes.objects.all(),
        'ourproperty': OurProperty.objects.all(),
        'about': About.objects.first(),
        'agency': Agency.objects.first(),
        'works': How_it_Works.objects.first(),
        'dating': Dating.objects.all(),
        'offer': Offer.objects.first(),
        'agents':Agent.objects.all(),
        'blog': OurBlog.objects.first(),
        'blog1': Blog.objects.all(),
        'contact': Contact.objects.all(),
        'infor': Information.objects.last(),
        'property': Property.objects.first(),
        'read': Read.objects.last(),
        'info': Info.objects.first(),
        'input': Input.objects.last(),
        'stayhome': Stayhome.objects.last(),
        'question': Question.objects.last(),
        'ouragent': OurAgent.objects.first()

    }
    return render(request, 'index.html', context)

def properties_single_view(request):
    return render(request, 'properties-single.html')

def properties_view(request):
    return render(request, 'properties.html')

def single_view(request):
    return render(request, 'single.html')

def send_message_view(request): 
    if request.method == 'POST':
        name = request.POST.get('name') 
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Input.objects.create(
            name  = name,
            email = email,
            subject = subject,
            message = message
        )
        return redirect('index-url')
        


  
