"""chaos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from user.views import UserCreateAPIView, UserLoginAPIView
from recipes.views import CategoryView, CategoryCreateView, MyRecipeView,RecipeView,RecipeCreateView, RecipeDeleteView,RecipeUpdateView, IngredientView, IngredientCreateView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('category/', CategoryView.as_view(), name='category-list'),
    path('category/create/', CategoryCreateView.as_view(), name='create-category'),
    path('recipe/', RecipeView.as_view(), name='recipe-list'),
    path('recipe/create/', RecipeCreateView.as_view(), name='create-recipe'),
    path('recipe/delete/<int:recipe_id>/', RecipeDeleteView.as_view(), name='delete-recipe'),
    path('recipe/edit/<int:recipe_id>/', RecipeUpdateView.as_view(), name='edit-recipe'),
    path('myrecipe/', MyRecipeView.as_view(), name='my_recipe_list'),
    path('ingredient/', IngredientView.as_view(), name='ingredient-list'),
    path('ingredient/create/', IngredientCreateView.as_view(), name='create-ingredient'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)