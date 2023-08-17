# apps/activities/admin.py
from django.contrib import admin
from apps.activities.models.interactiveactivity import InteractiveActivity

class InteractiveActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'activity_type', 'created_at', 'updated_at')
    search_fields = ('name', 'activity_type')
    list_filter = ('activity_type',)
    ordering = ('name',)

    fieldsets = (
        ("Activity Information", {
            'fields': ('name', 'description', 'activity_type')
        }),
        ("Timestamps", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(InteractiveActivity, InteractiveActivityAdmin)
