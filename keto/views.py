import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Recipe, KetoArticle


def index(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def keto_article_view(request):
    articles = KetoArticle.objects.all()
    return render(request, 'keto_article.html', {'articles': articles})

def article_detail_view(request, article_id):
    article = get_object_or_404(KetoArticle, id=article_id)
    return render(request, 'article_detail.html', {'article': article})
def recipes_view(request):
    recipes = Recipe.objects.all()
    dish_types = Recipe.objects.values_list('dish_type', flat=True).distinct()
    return render(request, 'recipes.html', {'recipes': recipes, 'dish_types': dish_types})

def get_recipes_view(request):
    dish_type = request.GET.get('type')

    # Получение списка блюд из модели Recipe на основе выбранного типа
    recipes = Recipe.objects.filter(dish_type=dish_type).values('title')

    # Преобразование QuerySet в список значений "title"
    recipes_list = [recipe['title'] for recipe in recipes]

    # Возврат шаблона с передачей списка рецептов и значения dish_type в контексте
    return render(request, 'recipes_detail.html', {'recipes': recipes_list, 'dish_type': dish_type})
