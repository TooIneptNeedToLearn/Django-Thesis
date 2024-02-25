from django.contrib import admin
from .models import Thesis

@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    list_display = ['title', 'authors', 'department', 'published_date', 'status']
    list_filter = ['status', 'published_date', 'department']
    search_fields = ['title', 'abstract', 'authors', 'advisors', 'keywords']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    ordering = ['status', 'published_date']