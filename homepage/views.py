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
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UploadForms()

    return render(request,"Uploads.html",{'form':form})