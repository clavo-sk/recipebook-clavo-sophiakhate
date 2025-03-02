from django.db import models

# Create your models here.

class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=100)

class Recipe(models.Model):
    recipeName = models.CharField(max_length=100)
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
