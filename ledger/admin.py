from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class IngredientAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]

class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient)