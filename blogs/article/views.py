from django.shortcuts import render
from .models import Category
# Create your views here.

def get_list_categories(request):
    categories = Category.objects.all()
    print(categories)
    return render(request, 'categories-list.html', {"categories": categories})