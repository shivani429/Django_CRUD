from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from .models import *
from demoapp.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


#django CRUD
def create_data(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        form = Details.objects.create(name = name, age = age, address = address) 
        form.save()
        return redirect('retrieve')
    return render(request,'details.html')
         
def retrieve(request):
    form = Details.objects.all()
    return render(request,'retrieve.html',{'form':form})  

def update1(request,id):
    object = Details.objects.get(id=id)
    if request.method == 'POST':
        if object:
            object.name = request.POST['name']
            object.age = request.POST['age']
            object.address = request.POST['address']
            object.save()
        return redirect('retrieve')
    return render(request,'editt.html',{'object':object})
    
def delete1(request,id):
    object = Details.objects.get(id=id)
    object.delete()
    return redirect('retrieve')   

