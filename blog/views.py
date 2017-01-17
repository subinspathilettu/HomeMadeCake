from django.shortcuts import render, get_object_or_404
from .models import Cake 

def post_list(request):
    cakes = Cake.objects.all()
    return render(request, 'blog/post_list.html', {'cakes' : cakes})

def cake_details(request, pk):
    cake = get_object_or_404(Cake, pk=pk)
    return render(request, 'blog/cake_details.html', {'cake' : cake})
