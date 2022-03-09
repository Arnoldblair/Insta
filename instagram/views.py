from difflib import context_diff
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from instagram.forms import UserRegistrationForm, UserLoginForm

# Create your views here.
def home_view(request):
    return render(request, "account/dashboard.html")




def register(request):
    contex={}
    if request.POST:
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context['register_form']=form


    else:
        form=UserRegistrationForm()
        context['register_form']=form
    return render(request, "account/register.html",context)


def login_view(request): 
    context={}
    if request.POST:
        form=UserLoginForm(request.POST)
        if form.is_valid():
            email=request.POST['email']

        password=request.POST['password']
        user=authenticate(request, email=email, password=password)


        if user is not None:
            login(request,user)
            return redirect("dashboard")

    else:
        form=UserLoginForm()
        context["login_forms"]=form
    return render(request, "account/login.html", context) 

def logout_view(request):
    logout(request)
    return redirect('login')


