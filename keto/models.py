from django.db import models

class Recipe(models.Model):
       title = models.CharField(max_length=100) #заголовок
       description = models.TextField() #Описание рецепта
       ingredients = models.TextField() #Список ингредиентов для рецепта
       instructions = models.TextField() #Шаги приготовления рецепта
       # Новое поле "тип блюда"
       dish_type = models.CharField(max_length=255, default='Unknown')
       created_at = models.DateTimeField(auto_now_add=True) #Дата и время создания рецепта (автоматически добавляется).

class KetoArticle(models.Model):
     title = models.CharField(max_length=100) #название
     content = models.TextField() #содержание
     author = models.CharField(max_length=50) #автор
     created_at = models.DateTimeField(auto_now_add=True) #дата и время создания

def __str__(self):
    return self.title
