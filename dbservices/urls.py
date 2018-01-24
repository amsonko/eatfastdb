from django.conf.urls import url
from . import views

urlpatterns = [
#     path('user/save/', views.save_user, name='save_user'),
#     path('user/<int:pk>/delete/', views.DeleteUser.as_view(), name='remove_user'),
#     path('user/login/', views.connect_user, name='connect_user'),
#     path('user/change_password/', views.change_password, name='change_password'),
#     path('recipe/save/', views.save_recipe, name='save_recipe'),
#     path('recipe/<int:pk>/', views.DetailRecipe.as_view(), name='detail_recipe'),
#     path('user/<int:pk>/delete/', views.DeleteRecipe.as_view(), name='remove_recipe'),
#     path('recipe/search/<str:query>', views.search_recipes, name='search_recipes'),
#     path('recipe/', views.List_Recipe, name='list_recipes'),
#     path('recipe/<int:recipe_id>/rate/', views.rate_recipe, name='rate_recipe'),
#     path('recipe/<int:recipe_id>/prevalidate/', views.prevalidate_recipe, name='prevalidate_recipe'),
#     path('recipe/<int:recipe_id>/validate/', views.validate_recipe, name='validate_recipe'),
#     path('ingredient/suggest/', views.suggest_ingredient, name='suggest_ingredient'),
#     path('ingredient/<int:ingredient_id>/prevalidate/', views.prevalidate_ingredient, name='prevalidate_ingredient'),
#     path('ingredient/<int:ingredient_id>/validate', views.validate_ingredient, name='validate_ingredient')
    url(r'^$', views.api_root),
    url(r'^ingredients/$', views.IngredientList.as_view()),
    url(r'^ingredients/(?P<pk>[0-9]+)/$', views.IngredientDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]