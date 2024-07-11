from django.shortcuts import render, redirect, reverse
from .models import Recipe, Ingredient, Comment
from users.models import CustomUser

# Create your views here.
def recipes(request):
    return render(request, "recipes/recipes.html",{
        "recipes": Recipe.objects.all()
    })

# get recipe page and comments on the recipe
def singleRecipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    comments = Comment.objects.filter(recipe=recipe)
    return render(request, 'recipes/recipe.html',{
        'recipe': recipe,
        'comments': comments,
        'recipe_id': recipe_id,
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

#add new comment
def addCmt(request, recipe_id):
    if request.method == "POST":
        content = request.POST.get('new-comment')
        recipe = Recipe.objects.get(pk=recipe_id)
        try:
            
            newComment = Comment.objects.create(
                parent_id=None,
                author= request.user,
                recipe= recipe,
                content = content
            )
            
            return redirect(reverse('recipes:recipe', kwargs={'recipe_id': recipe.id}))
        except Exception as e:
            print(f"Error: {e}")
            return render(request, "recipes/recipe.html", {
                "recipe": recipe,
                "comments": recipe.comments.all(),
                "message": f"An error occurred: {str(e)}"
            })    
    else:
        return redirect(reverse('recipes:recipe', kwargs={'recipe_id': recipe.id}))

#add a reply
# def addReply(request, recipe_id, parent_cmt_id):
#     if request.method == "POST":
#         content = request.POST.get('new-comment')
#         recipe = Recipe.objects.get(pk=recipe_id)
#         try:
#             newReply = Comment.objects.create(
#                 parent_id=parent_cmt_id,
#                 author= request.user,
#                 recipe= recipe,
#                 content = content
#             )
#             return redirect(reverse('recipes:recipe', kwargs={'recipe_id': recipe.id}))
#         except Exception as e:
#             print(f"Error: {e}")
#             return render(request, "recipes/recipe.html", {
#                 "recipe": recipe,
#                 "comments": recipe.comments.all(),
#                 "message": f"An error occurred: {str(e)}"
#             })    
#     else:
#         return redirect(reverse('recipes:recipe', kwargs={'recipe_id': recipe.id}))
        
            






#delete a comment
def deleteCmt(request, comment_id, recipe_id):
    if request.method == "POST":
        try:
            comment = Comment.objects.get(pk=comment_id)
            comment.delete()
            return redirect(reverse('recipes:recipe', kwargs={'recipe_id': recipe_id}))
        except Exception as e:
            print(f"Error: {e}")
            return render(request, "recipes/recipe.html", {
                "message": f"An error occurred: {str(e)}",
                "recipe_id": recipe_id
            })    
    else:
        return redirect(reverse('recipes:recipe', kwargs={'recipe_id': recipe_id}))

