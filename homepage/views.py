from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . models import Foodiee
from .models import FoodImages,Wishlist,Cart,FoodReview,CartItem
from django.contrib import messages
from . forms import UploadForms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout


# def Home(request):
#     return HttpResponse("Welcome to Django Home page")
# Create your views here.

#instead of sending response like this lets render our html page
# Foodiee = [{"name":"Food1","Desc":"Ready to eat food."},{"name":"Food2","Desc":"Ready to eat food2."},{"name":"Food3","Desc":"Ready to eat food3."}]

def Home(request):
    Foodiees = FoodImages.objects.all() #to display all the data in db
    context = {'Foodiees':Foodiees}
    return render(request,"Home.html",context)


def About(request):
    return render(request,"About.html")



@login_required(login_url="/Login")
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
        images = FoodImages.objects.all()

    return render(request,"Uploads.html",{'form':form,'images':images})





def login_page(request):
     if request.method == 'POST':
         form = AuthenticationForm(request,data=request.POST)
        #  print("Is form valid",form)
         if form.is_valid():
             #username #password 
            user_name = form.cleaned_data.get('username')  
            password = form.cleaned_data.get('password')
            user = authenticate(username=user_name,password=password)
            if user is not None:
                login(request,user)
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
    
def logout_user(request):
    logout(request)
    return redirect('home')

from django.shortcuts import get_object_or_404

def product_view(request,id):
    product = get_object_or_404(FoodImages,id=id)
    review_obj = FoodReview.objects.filter(product=product)

    return render(request,"Product.html",{'product':product,"review_obj":review_obj})

def wish_list(request,id):
    product = FoodImages.objects.get(id=id)
    obj1,created = Wishlist.objects.get_or_create(user= request.user)
    obj1.product.add(product)    
    obj1.save()
    return redirect('home')


#add to cart list
def cart_list(request,id):

#check if user has cart or not
    user_cart,created = Cart.objects.get_or_create(user= request.user)
# fetch the product with given id
    product = FoodImages.objects.get(id=id)

#create a cart with cart items using user and product
    cart_item, created = CartItem.objects.get_or_create(user=user_cart,product=product)
    cart_item.product = product 
    cart_item.save()
    return redirect('home')


#Show list of cart items
def show_cartList(request):
    cart,created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart = cart)
    return render(request, "CartList.html",{"user_products":cart_items})

def show_wishList(request):
    user = request.user
    wishlists = Wishlist.objects.filter(user=user) 
    
    # Collect all products from all wishlists
    products_with_wishlist = []
    for wishlist in wishlists:
        #add each product along with wishlist ID
        for product in wishlist.product.all():
            products_with_wishlist.append({
               'product' : product,
               'wishlist_id':wishlist.id  #includes wishlist id
            })   
    return render(request, "WishList.html", {"view_products": products_with_wishlist})




def remove_wish(request, id):
    if request.user.is_authenticated:
        wishlist_item = get_object_or_404(Wishlist,id=id,user=request.user)
        wishlist_item.delete()
        return redirect('home')
    else:
        return redirect('login')

from django.http import JsonResponse

def show_api(request):
    start_text = request.GET.get('parameter1')
    FoodName = FoodImages.objects.filter(name__startswith = start_text).values_list()
    if FoodName:
        message = {
            "FoodName": FoodName[0],
            "name":"Hey this is my data"
        }
    else:
        message = {
        "name":"data not found"
    }
    return JsonResponse(message)


  


