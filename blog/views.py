from django.shortcuts import render
from .models import Cake 

def post_list(request):
    cakes = Cake.objects.all()
    return render(request, 'blog/post_list.html', {'cakes' : cakes})
