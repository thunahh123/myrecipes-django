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

class Unit(models.Model):
    unit = models.CharField(max_length=40)
    abbr = models.CharField(max_length=25, null=True)
    plural = models.CharField(max_length=40)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
         return f"{self.unit}"

class Comment(models.Model):
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, related_name="replies", null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="comments", null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.recipe}'