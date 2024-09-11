from django.urls import path
from .import views



urlpatterns = [
    path('',views.Home,name="home"),
    path('About',views.About,name="about"),
    path('Upload',views.Uploads,name="upload_images"),
    path('Login',views.login_page,name="Login"),
    path('SignUp',views.SignUp,name="SignUp"),

    
]