from django.shortcuts import render, get_object_or_404
from .models import Cake
from django.contrib.auth.models import User
from .forms import CakeForm, RegisterForm
import logging

logger = logging.getLogger(__name__)

def post_list(request):
    cakes = Cake.objects.all()
    return render(request, 'blog/post_list.html', {'cakes' : cakes})

def cake_details(request, pk):
    cake = get_object_or_404(Cake, pk=pk)
    return render(request, 'blog/cake_details.html', {'cake' : cake})

def cake_new(request):
    if request.method == "POST":
        form = CakeForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            # commit=False means that we don't want to save the Post model yet
            cake = form.save(commit=False)
            cake.author = request.user
            cake.save()
            return redirect('cake_detail', pk=cake.pk)
    else:
        form = CakeForm()
    return render(request, 'blog/cake_edit.html', {'form': form})

def profile(request):
    if request.user.is_authenticated:
        cakes = Cake.objects.filter(vendor=request.user)
        return render(request, 'blog/profile.html', {'cakes' : cakes})
    else:
        return post_list(request)

def register(request):
    if request.method == "POST":
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid:
            user = registerForm.save(commit=True)
            user.save()
            return post_list(request)
    else:
        registerForm = RegisterForm()
    return render(request, 'blog/register.html', {'form': registerForm}) 