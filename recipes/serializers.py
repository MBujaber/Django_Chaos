from rest_framework import serializers
from recipes.models import Category, Recipe, Ingredient

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', "image"]


class CategoryCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Category
        fields = ['user','title', "image"]

        

class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['ingredient', 'title', "user",'image', "category"]


class RecipeCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Recipe
        fields = ['ingredient','title', "user",'image', "category"]

class RecipeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['ingredient','title','image', "category"]