from django.shortcuts import render
from .models import Recipe, Ingredient
#from users.models import CustomUser

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


def addRecipe(request):
    if request.method == 'POST':
        name = request.POST.get('rname')
        time = request.POST.get('time')
        servings = request.POST.get('servings')
        desc = request.POST.get('desc')
        dir = request.POST.get('dir')

        try:
            new_recipe = Recipe.objects.create(
                name=name,
                time=time,
                servings=servings,
                description=desc,
                direction=dir,
                author=  request.user   # Use the logged-in user as the author
            )

            print(f"New recipe created: {new_recipe}")

            return render(request, "recipes/addRecipe.html",{
                "message": "Successfully added a new recipe!"
            })
        except Exception as e:
            print(f"Error: {e}")
            return render(request, "recipes/addRecipe.html", {
                "message": f"An error occurred: {str(e)}"
            })       
    
    else:
        # Render the form to add a new recipe
        return render(request, "recipes/addRecipe.html")



#add ingredients
def addIng(request):
    if request.method == 'POST':
        name = request.POST.get('iname')
        try:
            if Ingredient.objects.filter(name=name).exists():
                return render(request, "recipes/addIngredient.html",{
                "message": "Ingredient already exists!"
                })
            else:
                new_ingredient = Ingredient.objects.create(name=name)

                print(f"New ingredient created: {new_ingredient}")

                return render(request, "recipes/addIngredient.html",{
                    "message": "Successfully added a new ingredient!"
                })
        except Exception as e:
            print(f"Error: {e}")
            return render(request, "recipes/addIngredient.html", {
                "message": f"An error occurred: {str(e)}"
            })       
    
    else:
        # Render the form to add a new recipe
        return render(request, "recipes/addIngredient.html")
