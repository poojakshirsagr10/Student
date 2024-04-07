from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.
def user_login(request):
    template_name = "auth_app/login.html"
    if request.method == "POST":
        un = request.POST["un"]
        pw = request.POST["pw"]
        user = authenticate(username=un , password=pw)
        if user:
            login(request, user)
            return redirect('show_url')
        else:
            return HttpResponse("plz correct username or password")
    return render(request, template_name)


def user_signup(request):
    template_name = "auth_app/register.html"
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("registration success")
    context={"form":form}
    return render(request,template_name, context)


def user_logout(request):
    logout(request)
    return redirect("login_url")