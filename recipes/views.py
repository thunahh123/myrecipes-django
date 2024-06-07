from django.shortcuts import render
from .models import Recipe

# Create your views here.
def recipes(request):
    return render(request, "recipes/recipes.html",{
        "recipes": Recipe.objects.all()
    })

def singleRecipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'recipes/recipe.html',{
        'recipe': recipe
    })

# def add(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         time = request.POST.get('time')
#         servings = request.POST.get('servings')
#         desc = request.POST.get('description')
#         dir = request.POST.get('direction')
#         author = 


#     new = Recipe.objects.create(
#               name = name
#               time = time
#           )