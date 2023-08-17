from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from apps.users.models.user import User
from apps.users.models.patient import Patient


class UserAdmin(DefaultUserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 
                'username', 
                'first_name', 
                'last_name', 
                'password1', 
                'password2'
            ),
        }),
    )
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    ordering = ('email',)

admin.site.register(User, UserAdmin)


class PatientAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'user_email', 'family_name', 'given_name', 'gender', 'birth_date', 'phone')
    search_fields = ('identifier', 'user__email', 'family_name', 'given_name', 'gender', 'phone')
    list_filter = ('gender', 'active', 'birth_date')
    ordering = ('family_name', 'given_name')

    fieldsets = (
        ('User Info', {
            'fields': ('user', 'user_email')
        }),
        ('Personal Details', {
            'fields': ('identifier', 'active', 'family_name', 'given_name', 'middle_name', 'suffix', 'prefix', 'nickname', 'gender', 'birth_date')
        }),
        ('Contact', {
            'fields': ('address', 'phone', 'email', 'language')
        }),
        ('Other', {
            'fields': ('marital_status', 'photo')
        }),
    )

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'User Email'

admin.site.register(Patient, PatientAdmin)
