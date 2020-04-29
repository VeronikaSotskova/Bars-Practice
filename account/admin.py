from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.forms import CustomUserCreationForm, CustomUserChangeForm
from account.models import CustomUser, Room


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    form = CustomUserChangeForm
    list_display = ('username', 'first_name', 'last_name', 'position', 'room')
    search_fields = ('username',)
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'username', 'position', 'password', 'room')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'password1', 'password2', 'position')}
         ),
    )


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)
