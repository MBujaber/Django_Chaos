from rest_framework import serializers
from recipes.models import Category

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']
