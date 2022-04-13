from email import message
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Customform
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        register_form = Customform(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New User Account has been created, Login To get started!"))
        return redirect('register')
    else:
        register_form = Customform()
    return render(request, 'register.html', {'register_form':register_form})