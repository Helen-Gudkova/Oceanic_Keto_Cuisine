import json

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Recipe, KetoArticle, Menu
from django.db.models import Q



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

def menu_view(request):
    days_of_week = Menu.DAYS_OF_WEEK  # Получаем список дней недели
    meal_time = request.GET.get('meal_time')  # Получаем время приема пищи
    # menu = Menu.objects.filter(day=day, meal_time=meal_time)
    return render(request, 'view_menu.html', {
        # 'menu': menu,  # Передаем экземпляры Menu
        'days_of_week': days_of_week,
        'meal_time': meal_time,
    })
def menu_detail_view(request):
    day = request.GET.get('day')  # Получаем день из GET-параметров
    menu_items = Menu.objects.filter(day=day).order_by('meal_time')
    return render(request, 'menu_detail.html', {'menu_items': menu_items, 'day': day})


def get_recipes_view(request):
    dish_type = request.GET.get('type')

    # Получение списка блюд из модели Recipe на основе выбранного типа
    recipes = Recipe.objects.filter(dish_type=dish_type).values('title')

    # Преобразование QuerySet в список значений "title"
    recipes_list = [recipe['title'] for recipe in recipes]

    # Возврат шаблона с передачей списка рецептов и значения dish_type в контексте
    return render(request, 'recipes_detail.html', {'recipes': recipes_list, 'dish_type': dish_type})

def recipe_detail(request, recipe_title):
    recipe = get_object_or_404(Recipe, title=recipe_title)
    return render(request, 'recipes_detail_detail.html', {'recipe': recipe})

def recipe_detail_detail(request, recipe_title):
    recipe = Recipe.objects.get(title=recipe_title)
    recipes = Recipe.objects.all() # получаем список всех рецептов
    context = {'recipe': recipe, 'recipes': recipes} # передаем список рецептов в контекст
    return render(request, 'recipes_detail_detail.html', context)

def recipe_search(request):
    query = request.GET.get('search_query')
    recipes = Recipe.objects.filter(Q(title__icontains=query) | Q(ingredients__icontains=query))
    context = {
        'recipes': recipes,
    }
    return render(request, 'recipes_search.html', context)
