from django.shortcuts import render
from home_page.models import Register

def home(request):
    query = Register.objects.all()
    print(query)
    context = {"data":query}  
    return render(request,"home.html",context)

def signup(request):
    query = Register.objects.all()
    print(query)
    context = {"data":query}
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email= request.POST.get('email')
        pwd=request.POST.get('password')
        print(firstname,lastname,email,pwd)
        query = Register(firstname=firstname,lastname=lastname,email=email,pwd=pwd)
        query.save()
        print("data saved successfully")
        
    return render(request,"signup.html")


# Create your views here.
