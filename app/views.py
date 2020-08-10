from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import contactform
from django.contrib.auth.models import User, auth



# Create your views here.


def home(request):
    print("submit the insert")
    # contact1 = contactform.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        description = request.POST['description']

        contactform1 = contactform(name=name,email=email,description=description)
        contactform1.save()
        print('user created')
        return redirect('home')


    else:
        return render(request, 'home.html')



def voting(request):
    return render(request, 'voting.html')

def textutils(request):
    return render(request, 'textutils.html')

def pinggame(request):
    return render(request, 'pinggame.html')

def chatbot(request):
    return render(request, 'chatbot.html')

def sportcenter(request):
    return render(request, 'sportcenter.html')