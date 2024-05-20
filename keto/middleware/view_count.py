from django.shortcuts import get_object_or_404
from keto.models import Recipe

class ViewCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if 'recipe_title' in view_kwargs:
            recipe_title = view_kwargs['recipe_title']
            recipe = get_object_or_404(Recipe, title=recipe_title)
            recipe.views_count += 1
            recipe.save()
        return None