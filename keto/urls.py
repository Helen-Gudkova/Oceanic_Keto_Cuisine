# /keto/urls.py
from django.urls import path
from keto import views
from keto.views import about_view

# Префикс /keto/
urlpatterns = [
    path('about/', about_view, name='about'),

]