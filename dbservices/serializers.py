from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .models import Ingredient

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    suggested_ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    class Meta:
        model = User
        fields = ('url','username', 'email', 'first_name', 'last_name', 'is_active', 'suggested_ingredients')

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    inguser = serializers.ReadOnlyField(source='inguser.username')
    class Meta:
        model = Ingredient
        fields = ('ingname', 'ingtype', 'ingnutvalue', 'inguser')