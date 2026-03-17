from django.contrib import admin
from main.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','email', 'last_login', 'is_superuser', 'is_staff','is_active']
    list_display_links = ['email']