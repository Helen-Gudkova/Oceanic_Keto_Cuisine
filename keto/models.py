from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Avg
class Recipe(models.Model):
    title = models.CharField(max_length=100) #заголовок
    description = models.TextField() #Описание рецепта
    ingredients = models.TextField() #Список ингредиентов для рецепта
    instructions = models.TextField() #Шаги приготовления рецепта
    # Новое поле "тип блюда"
    dish_type = models.CharField(max_length=255, default='Unknown')
    calories = models.IntegerField()  # Добавленное поле для калорий
    created_at = models.DateTimeField(auto_now_add=True) #Дата и время создания рецепта (автоматически добавляется)
    def __str__(self):
        return self.title
def average_rating(self):
    reviews = self.reviews.all()  # Получаем все отзывы для рецепта
    if reviews.exists():
        return reviews.aggregate(Avg('rating'))['rating__avg']
    return 0
class KetoArticle(models.Model):
     title = models.CharField(max_length=100) #название
     content = models.TextField() #содержание
     author = models.CharField(max_length=50) #автор
     created_at = models.DateTimeField(auto_now_add=True) #дата и время создания

def __str__(self):
    return self.title

def get_absolute_url(self):
    return reverse('recipe_detail', kwargs={'recipe_title': self.title})

class Menu(models.Model):
    DAYS_OF_WEEK = (
        ('Monday', 'Понедельник'),
        ('Tuesday', 'Вторник'),
        ('Wednesday', 'Среда'),
        ('Thursday', 'Четверг'),
        ('Friday', 'Пятница'),
        ('Saturday', 'Суббота'),
        ('Sunday', 'Воскресенье'),
    )
    MEAL_TIMES = (
        ('Breakfast', 'Завтрак'),
        ('Lunch', 'Обед'),
        ('Dinner', 'Ужин'),
        ('Snack', 'Перекус'),
    )
    meal_time = models.CharField(max_length=10, choices=MEAL_TIMES)
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def dish_name(self):
        return self.recipe.name

    def calories(self):
        return self.recipe.calories

    def __str__(self):
        return f"{self.day}: {self.recipe.title}"

class RecipeReview(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_reviews')
    rating = models.PositiveIntegerField(default=0)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('recipe', 'user')


