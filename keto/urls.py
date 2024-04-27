# /keto/urls.py
from django.urls import path, include
from django.conf import settings

from keto.views import about_view

# URL-шаблоны для префикс /keto/
urlpatterns = [
    path('about/', about_view, name='about'),
    ]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('debug/', include(debug_toolbar.urls)),
        # Другие URL-шаблоны для DEBUG
    ] + urlpatterns

# Возможно, вам нужно зарегистрировать админ-панель:
# from django.contrib import admin
# urlpatterns += [path('admin/', admin.site.urls)]
