from django.shortcuts import render
from . import models

def all_products_view(request):
    # Получаем все продукты, сортируем по убыванию id
    all_products = models.Product.objects.all().order_by('-id')
    
    # Создаем контекст для шаблона
    context = {
        'all_products': all_products,
    }
    
    # Возвращаем рендер с контекстом
    return render(request, 'tags/all_products.html', context)

def meal_view(request):
    meal = models.Product.objects.all().order_by('-id').filter(tags_name='Еда')
    context = {
        'meal': meal,
    }
    return render(request, 'tags/meals.html', context)

