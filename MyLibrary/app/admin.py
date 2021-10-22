from django.contrib import admin
from .models import BookDetails, CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id','email']

@admin.register(BookDetails)
class BookDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','user','book_name','author_name','quantity','date']