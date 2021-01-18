from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

'''
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
'''


@login_required
def index(request):
    return render(request, 'accounts/index.html')


def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'accounts/index.html')
    context['form'] = form
    return render(request, 'registration/sign_up.html', context)
