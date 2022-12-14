
from .models import Category,Recipe, Ingredient
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import  CategorySerializer, IngredientSerializer, RecipeSerializer,RecipeUpdateSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsCreator
from django_filters.rest_framework import DjangoFilterBackend

class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CategoryCreateView(CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RecipeView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    

class MyRecipeView(ListAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
            return Recipe.objects.filter(user=self.request.user)
            
        

class RecipeCreateView(CreateAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RecipeDeleteView(DestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'recipe_id'
    permission_classes = [IsCreator]    


class RecipeUpdateView(UpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'recipe_id'
    permission_classes = [IsCreator]


class IngredientView(ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [AllowAny]

class IngredientCreateView(CreateAPIView):
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)    