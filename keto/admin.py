
from django.contrib import admin

from .models import Recipe, KetoArticle, Menu


class DishTypeFilter(admin.SimpleListFilter):
    title = 'Тип блюда' # Название фильтра, которое будет отображаться в админке
    parameter_name = 'dish_type' # Имя параметра, который будет передаваться в URL

    def lookups(self, request, model_admin):
        """
        Метод для определения значений фильтрации
        Возвращает кортежи с двумя значениями: значение и отображаемое имя
        :param request:
        :param model_admin:
        :return:
        """
        return (
            ('UNCHECKED', 'Не проверено'),
            ('CHECKED', 'Проверено'),
        )

    def queryset(self, request, queryset):
        """
        Метод для фильтрации
        self.value() - получение значения фильтра
        :param request:
        :param queryset:
        :return:
        """
        if self.value() == 'UNCHECKED':
            return queryset.filter(check_status=0)
        if self.value() == 'CHECKED':
            return queryset.filter(check_status=1)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'ingredients', 'instructions', 'dish_type', 'calories','created_at')
    list_filter = ('dish_type', DishTypeFilter)
    search_fields = ('description', 'Category__name', 'Answer', 'tags__name')
    ordering = ('-created_at', 'description')
    list_per_page = 20
    readonly_fields = ('dish_type',)  # Использовать readonly_fields вместо fields


    def tags_list(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    tags_list.short_description = 'dish_type'

    def check_status(self, obj):
        # Логика для определения статуса проверки
        return obj.check_status
    check_status.short_description = 'Check Status'


    # list_editable = ('category_name',) # Редактируемое поле
    # Добавляем метод для отображения названия категории


    # Определение метода для отображения краткой информации о рецепте
    # ordering по полю answer, так как точного поля для сортировки по краткому описанию нет
    @admin.display(description="Шаги приготовления рецепта", ordering='instructions')
    def brief_info(self, Recipe):
        # Определяем длину ответа
        length = len(Recipe.instructions)
        # Проверяем наличие кода
        has_code = 'Да' if '```' in Recipe.instructions else 'Нет'
        return f"Длина ответа: {length}, Код: {has_code}"

    # Дополнительный метод для отображения вопросов

@admin.register(KetoArticle)
class CardTagsAdmin(admin.ModelAdmin):
    # Отображаемые поля
    list_display = ('title', 'content','author')
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('meal_time', 'day', 'recipe')

