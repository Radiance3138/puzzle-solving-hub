from django.contrib import admin
from .models import PuzzleHub, SourceTextEntry

class PuzzleHubAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'status', 'created_at')
    list_filter = ('status', 'created_at')


class SourceTextEntryAdmin(admin.ModelAdmin):
    list_display = ('cipher_text', 'method', 'key', 'solver', 'puzzle_hub', 'date_recorded', 'parent_entry')
    list_filter = ('method', 'date_recorded')


admin.site.register(PuzzleHub, PuzzleHubAdmin)
admin.site.register(SourceTextEntry, SourceTextEntryAdmin)