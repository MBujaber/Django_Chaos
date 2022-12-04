from django.contrib import admin
from .models import Category, Recipe, Ingredient

admin.site.register([Category, Recipe, Ingredient])