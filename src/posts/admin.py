from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("username", "title", "created_datetime")
    search_fields = ("username", "title", "content")
    readonly_fields = ("created_datetime",)
