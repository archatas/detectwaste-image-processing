from django.contrib import admin

from .models import Category, ProcessedImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]


@admin.register(ProcessedImage)
class ProcessedImageAdmin(admin.ModelAdmin):
    list_display = ["created_at", "image", "status"]
    list_filter = ["status", "categories"]
    filter_horizontal = ["categories"]
