from rest_framework import serializers
from recipes.models import Category, Recipe, Ingredient

# class CategoryListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'title', "image"]


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'user','title', "image"]

        

class RecipeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Recipe
        fields = ['id', 'ingredient','title', "user", "category",'image']

class RecipeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['ingredient','title','image', "category"]