from django.contrib import admin
from .models import TrickCategory, SkateTrick, UserProgress

@admin.register(TrickCategory)
class TrickCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(SkateTrick)
class SkateTrickAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'difficulty', 'created_at')
    list_filter = ('category', 'difficulty')
    search_fields = ('name', 'description')
    date_hierarchy = 'created_at'

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'trick', 'status', 'last_practiced')
    list_filter = ('status', 'trick__category', 'trick__difficulty')
    search_fields = ('user__username', 'trick__name', 'notes')
    date_hierarchy = 'last_practiced' 