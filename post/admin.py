from django.contrib import admin 
from django.contrib.admin import ModelAdmin
from .models import Post

# Register your models here.

#admin.site.register(Todo)

class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'title','body', 'created_at' , 'modified_at')
admin.site.register(Post, BookAdmin)

