from rest_framework import generics
from django.contrib.auth.models import User
from .models import Ingredient
from .serializers import IngredientSerializer, UserSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'ingredients': reverse('ingredient-list', request=request, format=format)
    })
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
        
class IngredientList(generics.ListCreateAPIView):
    """list all ingredients, or create a new ingredient"""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(inguser=self.request.inguser)
    
class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    """ retrieve, update or delete an ingredient """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)