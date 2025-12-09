from django.contrib import admin
from .models import PuzzleHub, SourceTextEntry

@admin.register(PuzzleHub)
class PuzzleHubAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description')
    raw_id_fields = ('owner', 'participants')
    autocomplete_fields = ('owner', 'participants')

@admin.register(SourceTextEntry)
class SourceTextEntryAdmin(admin.ModelAdmin):
    list_display = ('cipher_text', 'method', 'key', 'solver', 'puzzle_hub', 'date_recorded', 'parent_entry')
    list_filter = ('method', 'date_recorded')
    search_fields = ('cipher_text', 'plain_text')
    raw_id_fields = ('parent_entry', 'puzzle_hub', 'solver')
    autocomplete_fields = ('parent_entry', 'puzzle_hub', 'solver')
    date_hierarchy = 'date_recorded'