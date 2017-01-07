from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import BlogsModel

class BlogsAdmin(ModelAdmin):
    model = BlogsModel
    list_display = ("title", "discoverable")
    readonly_fields = ("_id",)
    search_fields = ("title", "content", "_id")
    def Mark_Selected_Discoverable(modeladmin, request, queryset):
        queryset.update(discoverable=True)
    def Mark_Selected_Undiscoverable(modeladmin, request, queryset):
        queryset.update(discoverable=False)
    actions = (Mark_Selected_Discoverable, Mark_Selected_Undiscoverable)

admin.site.register(BlogsModel, BlogsAdmin)
