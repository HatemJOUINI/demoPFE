from django.shortcuts import render, redirect
from django import forms
from pfe.forms import FormCan
from django.http import HttpResponseRedirect, HttpResponse
from pfe.models import Candidat
from django.core.mail import send_mail

# Create your views here.
def emp (request): 
    if request.method == "POST":  
        form = FormCan(request.POST)  
        if form.is_valid():    
            form.save()
            send_mail(subject="accusé reception",
             message="Félicitation, votre candidature a été sauvegardée avec succès", 
            from_email="hateem.juini@gmail.com",
        recipient_list=[form.cleaned_data['e_mail']],
        auth_user = 'hateem.juini@gmail.com',
    auth_password = 'testdjango',
    fail_silently = False,
        )
            return HttpResponseRedirect('/message/') 
            
        else:
            return HttpResponse('<h2>veuillez entrer des données valides </h2>')
             
    else:  
        form = FormCan()  
    return render(request,'index.html',{'form':form }) 


def message(request):
    return HttpResponse('<h1>Félicitation, votre candidature a été sauvegardée avec succès</h1>')


def admin(request):
    candidats=Candidat.objects.all()
    return render(request,'admin.html',{'candidats':candidats }) 