from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicado','autor')
    date_hierarchy = 'publicado'
    search_fields = ('titulo','descricao')