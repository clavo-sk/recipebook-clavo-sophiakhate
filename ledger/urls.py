from django.urls import path
from . import views

urlpatterns = [
    path('recipes/list', views.list, name='recipes'),
    path('recipe/1', views.recipe1, name='recipe'),
    path('recipe/2', views.recipe2, name='recipe'),
]

app_name = "ledger"



