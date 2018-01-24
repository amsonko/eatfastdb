from .models import Recipe
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

class DetailView(generic.DetailView):
    model = Recipe