from django.db import models

# Create your models here.

class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=100)
    
    def __str__(self):
        return '{}'.format(self.ingredientName)
        
    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.ingredientName)])

class Recipe(models.Model):
    recipeName = models.CharField(max_length=100)
    
    def __str__(self):
        return '{}'.format(self.recipeName)
        
    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.recipeName)])
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
