from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название рецепта")
    description = models.TextField(verbose_name="Описание рецепта")

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название ингредиента")
    quantity = models.IntegerField(verbose_name="Количество ингредиента")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name="Рецепт")

    def __str__(self):
        return f"{self.name} ({self.quantity})"