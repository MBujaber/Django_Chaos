from django.contrib.auth.models import User
from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return f"{self.id}: {self.title}"

class Ingredient(models.Model):
   name = models.CharField(max_length=100)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   
   def __str__(self):
        return f"{self.name}"


class Recipe(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="categories"
    )
    ingredient = models.ManyToManyField(Ingredient, related_name="recipies")
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return f"{self.id}:{self.user.username}: {self.title}"