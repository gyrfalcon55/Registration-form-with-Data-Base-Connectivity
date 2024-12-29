from django.urls import path
from home_page import views

urlpatterns = [
    path('',views.signup,name="signup"),
    path('home',views.home,name="home"),
    path('update/<id>',views.update,name="update"),
    path('delete/<id>',views.delete,name="deletedata")

]
