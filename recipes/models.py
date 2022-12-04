from django.contrib.auth.models import User
from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")
    image = models.ImageField()


    def __str__(self):
        return self.title

class Recipe(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="categories"
    )
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipies")
    image = models.ImageField()

    def __str__(self):
        return f"{self.user.username}: {self.title}"


class Ingredient(models.Model):
   recipe = models.ManyToManyField(Recipe, related_name="recipies")
   name = models.CharField(max_length=100)
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ingredients")
   
   def __str__(self):
        return f"{self.recipe}: {self.user.username}: {self.name}"