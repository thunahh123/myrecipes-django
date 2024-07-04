from django.db import models
from users.models import CustomUser
#from django.forms import ModelForm

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=40)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}"
    

class Recipe(models.Model):
    name = models.CharField(max_length=64)
    time = models.IntegerField()
    servings = models.IntegerField()
    description = models.TextField()
    direction = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="recipes", null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    def __str__(self) :
        return f":{self.name}: {self.description} (Created by: {self.author}) "
    
class IngredientRecipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    # recipes =  models.ManyToManyField(Recipe, blank=True, related_name="ingredients")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    # def __str__(self):
    #     return f"{self.name}"

