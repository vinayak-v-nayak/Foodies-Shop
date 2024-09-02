from django.shortcuts import render
from django.http import HttpResponse
from .models import Foodiee



# def Home(request):
#     return HttpResponse("Welcome to Django Home page")
# Create your views here.

#instead of sending response like this lets render our html page
# Foodiee = [{"name":"Food1","Desc":"Ready to eat food."},{"name":"Food2","Desc":"Ready to eat food2."},{"name":"Food3","Desc":"Ready to eat food3."}]

def Home(request):
    Foodiees = Foodiee.objects.all()
    context = {'Foodiee':Foodiees}
    return render(request,"Home.html",context)


def About(request):
    return render(request,"About.html")