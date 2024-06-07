from django.urls import path

from . import views

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('<int:recipe_id>', views.singleRecipe, name='recipe'),
    # path('add', views.add, name="add"),
]
