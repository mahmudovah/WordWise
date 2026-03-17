from django.contrib import admin
from asosiy.models import Subject, Word
# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'author__first_name', 'created_at', 'updated_at']
    list_display_links = ['title']

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ['id','word','translated','author__first_name','created_at', 'updated_at']
    list_display_links =['word']
    search_fields = ['word', 'translated']
    list_filter =['author']
    prepopulated_fields = {'slug':('word',)}