from django.contrib import admin

# Register your models here.
from .models import User, Ingredient,SuperUser,Utensil,Action,Recipe,Note


admin.site.register(User)
# admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(SuperUser)
admin.site.register(Utensil)
admin.site.register(Action)
admin.site.register(Recipe)
admin.site.register(Note)

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('ingname', 'ingtype', 'ingnutvalue', 'inguser', 'ingspuser')
    list_display_links = ('ingname',)
    list_editable = ('ingtype', 'ingnutvalue')
    list_filter = ('ingtype', 'ingname')
    fields = ('ingtype', ('ingname', 'ingnutvalue'), ('inguser', 'ingspuser'))
#     readonly_fields = ('inguser', 'ingspuser')
    search_fields = ['ingname', 'ingtype', 'inguser__username', 'ingspuser__supername']
    lis_per_page = 2
