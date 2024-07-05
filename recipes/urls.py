from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('<int:recipe_id>', views.singleRecipe, name='recipe'),
    path('add', views.addRecipe, name="add"),
    path('ingredients/add', views.addIng, name="addIng"),
    path('<int:recipe_id>/addComment', views.addCmt, name="addCmt"),

    
]
