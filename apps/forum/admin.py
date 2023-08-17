from django.contrib import admin

from apps.forum.models.forum import Forum
from apps.forum.models.forumcomment import ForumComment
from apps.forum.models.message import Message
from apps.forum.models.resource import Resource


class ForumAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

    fieldsets = (
        ("Forum Information", {
            'fields': ('title', 'description')
        }),
        ("Timestamps", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


class ForumCommentAdmin(admin.ModelAdmin):
    list_display = ('forum', 'user', 'content', 'created_at', 'updated_at')
    search_fields = ('content',)
    ordering = ('-created_at',)
    raw_id_fields = ('forum', 'user')

    fieldsets = (
        ("Comment Information", {
            'fields': ('forum', 'user', 'content')
        }),
        ("Timestamps", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'content', 'created_at', 'updated_at')
    search_fields = ('content',)
    ordering = ('-created_at',)
    raw_id_fields = ('sender', 'recipient')

    fieldsets = (
        ("Message Details", {
            'fields': ('sender', 'recipient', 'content')
        }),
        ("Timestamps", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'resource_type', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('resource_type',)
    ordering = ('-created_at',)

    fieldsets = (
        ("Resource Information", {
            'fields': ('title', 'content', 'resource_type')
        }),
        ("Timestamps", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Forum, ForumAdmin)
admin.site.register(ForumComment, ForumCommentAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Resource, ResourceAdmin)
