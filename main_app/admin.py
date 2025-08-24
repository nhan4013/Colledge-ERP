from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import *


class UserModel(UserAdmin):
    model = CustomUser
    list_display = ('email', 'user_type', 'gender')
    list_filter = ('user_type', 'gender')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('user_type', 'gender', 'profile_pic', 'address', 'fcm_token')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'user_type', 'gender', 'profile_pic', 'address', 'fcm_token', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}
        ),
    )


admin.site.register(CustomUser,UserModel)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Book)
admin.site.register(IssuedBook)
admin.site.register(Library)
admin.site.register(Subject)
admin.site.register(Session)
