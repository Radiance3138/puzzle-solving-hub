from django.contrib import admin
from .models import ArgUserProfile, Friendship

@admin.register(ArgUserProfile)
class ArgUserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_name', 'bio', 'date_joined')
    list_filter = ('date_joined',)
    search_fields = ('user__username', 'display_name')
    raw_id_fields = ('friends',)
    autocomplete_fields = ('friends',)

@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('from_user__username', 'to_user__username')
    raw_id_fields = ('from_user', 'to_user')
    autocomplete_fields = ('from_user', 'to_user')
    date_hierarchy = 'created_at'