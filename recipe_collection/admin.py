from django.contrib import admin
from .models import Recipe, Profile

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('headline', 'posted_by', 'date_posted')
    list_filter = ('posted_by', 'date_posted')
    search_fields = ('headline', 'description', 'ingredients', 'preparation')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username', 'bio')
