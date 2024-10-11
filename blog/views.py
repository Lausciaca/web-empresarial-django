from django.shortcuts import render, get_object_or_404
from .models import Category, Post

# Create your views here.
def blog(request):
    return render(request, 'blog/blog.html', {
        'categories': Category.objects.all,
        'posts': Post.objects.all
    })
    
def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'blog/category.html', {'category':category})
