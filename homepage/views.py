from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Foodiee
from . forms import UploadForms


# def Home(request):
#     return HttpResponse("Welcome to Django Home page")
# Create your views here.

#instead of sending response like this lets render our html page
# Foodiee = [{"name":"Food1","Desc":"Ready to eat food."},{"name":"Food2","Desc":"Ready to eat food2."},{"name":"Food3","Desc":"Ready to eat food3."}]

def Home(request):
    Foodiees = Foodiee.objects.all() #to display all the data in db
    context = {'Foodiee':Foodiees}
    return render(request,"Home.html",context)


def About(request):
    return render(request,"About.html")

def Uploads(request):
    if request.method == 'POST':
        form = UploadForms(request.POST,request.FILES)
        print(request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UploadForms()

    return render(request,"Uploads.html",{'form':form})


from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate

def login_page(request):
     if request.method == 'POST':
         form = AuthenticationForm(request,data=request.POST)
         print("Is form valid",form)
         if form.is_valid():
             #username #password 
            user_name = form.cleaned_data.get('username')  
            password = form.cleaned_data.get('password')
            user = authenticate(username=user_name,password=password)
            if user is not None:
                return  redirect('home')
            else:
                return render(request,"login.html",{'form':form})
     else:
        form = AuthenticationForm()
        return render(request,"login.html",{'form':form})

def SignUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Login') 
    else:
        form = UserCreationForm()
        return render(request,"SignUp.html",{'form':form})