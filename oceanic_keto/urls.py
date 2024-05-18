"""
URL configuration for oceanic_keto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from keto import views
from django.conf import settings
from django.conf.urls.static import static
from keto.views import recipes_view, menu_view, about_view, get_recipes_view, keto_article_view, article_detail_view, \
    menu_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', about_view, name='about'),
    path('keto_article/', keto_article_view, name='keto_article'),
    path('articles/<int:article_id>/', article_detail_view, name='article_detail'),
    path('recipes/', recipes_view, name='recipes'),
    path('menu/', menu_view, name='menu'),
    path('menu_detail/', menu_detail_view, name='menu_detail'),
    path('get-recipes/', get_recipes_view, name='get-recipes'),
    path('recipes/<str:recipe_title>/detail/<str:error_message>/', views.recipe_detail_detail, name='recipe_detail_detail'),
    path('recipes/search/', views.recipe_search, name='recipe_search'),
    path('recipes/<int:recipe_id>/create_review/', views.create_review, name='create_review'),
    path('recipe/<str:recipe_title>/', views.recipe_detail, name='recipe_detail'),
    path('keto/', include('keto.urls')),
    path('users/', include('users.urls', namespace='users')),  # Подключение URL-путей из приложения users

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
