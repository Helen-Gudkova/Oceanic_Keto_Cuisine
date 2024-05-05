import json

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Recipe, KetoArticle, Menu, RecipeReview
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe, RecipeReview
from .forms import ReviewForm
from django.db.models import Avg



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
    day_name = dict(Menu.DAYS_OF_WEEK).get(day)  # Получаем название дня
    total_calories = sum(int(item.calories() or 0) for item in menu_items)
    meal_time_groups = {}
    for item in menu_items:
        meal_time_groups.setdefault(item.get_meal_time_display(), []).append(item)

    return render(request, 'menu_detail.html', {
        'day': day,
        'day_name': day_name,  # Добавляем day_name в контекст
        'total_calories': total_calories,
        'meal_time_groups': meal_time_groups,
    })


def get_recipes_view(request):
    dish_type = request.GET.get('type')

    # Получение списка объектов Recipe с аннотацией среднего рейтинга
    recipes = Recipe.objects.filter(dish_type=dish_type).annotate(average_rating=Avg('reviews__rating'))

    # Создание списка словарей с информацией о рецептах и их рейтингах
    recipes_data = [
        {'title': recipe.title, 'rating': recipe.average_rating}  # Доступ к аннотации
        for recipe in recipes
    ]

    # Передача данных в контексте шаблона
    return render(request, 'recipes_detail.html', {'recipes_data': recipes_data, 'dish_type': dish_type})
def recipe_detail(request, recipe_title):
    recipe = get_object_or_404(Recipe, title=recipe_title)
    # Фильтруем отзывы по текущему рецепту
    reviews = RecipeReview.objects.filter(recipe=recipe)

    context = {
        'recipe': recipe,
        'reviews': reviews,
         }
    return render(request, 'recipes_detail_detail.html', context)

def recipe_detail_detail(request, recipe_title, error_message=None):
    recipe = get_object_or_404(Recipe, title=recipe_title)
    reviews = RecipeReview.objects.filter(recipe=recipe)
    error_message = request.GET.get('error_message')  # Получаем error_message из запроса
    recipes = Recipe.objects.all()
    user_review = RecipeReview.objects.filter(recipe=recipe, user=request.user).first()

    context = {
        'recipe': recipe,
        'recipes': recipes,
        'reviews': reviews,
        'user_review': user_review,
        'error_message': error_message,  # Добавляем error_message в контекст
    }
    return render(request, 'recipes_detail_detail.html', context)
def recipe_search(request):
    query = request.GET.get('search_query')
    recipes = Recipe.objects.filter(Q(title__icontains=query) | Q(ingredients__icontains=query))
    context = {
        'recipes': recipes,
    }
    return render(request, 'recipes_search.html', context)

@login_required
def create_review(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_exists = RecipeReview.objects.filter(recipe=recipe, user=request.user).exists()
            if review_exists:
                error_message = 'Вы уже оставили отзыв на этот рецепт.'
                return redirect('recipe_detail_detail', recipe_title=recipe.title, error_message=error_message)
            else:
                review = form.save(commit=False)
                review.recipe = recipe
                review.user = request.user
                review.save()
                error_message = None  # Здесь устанавливаем error_message в None после успешного сохранения отзыва
                return redirect('recipe_detail_detail', recipe_title=recipe.title, error_message=error_message)
    else:
        form = ReviewForm()

    context = {
        'recipe': recipe,
        'form': form,
    }
    return render(request, 'create_review.html', context)



