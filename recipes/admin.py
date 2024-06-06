from django.contrib import admin
from .models import Recipe, User, Ingredient

# Register your models here.
admin.site.register(Recipe)
admin.site.register(User)
admin.site.register(Ingredient)

