from django.contrib import admin
from botapp.models import BotUser

# Register your models here.


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','chat_id','username','joined_at','is_active']
    list_display_links = ['full_name']
    readonly_fields = ['chat_id']