from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.authentication import UserModel
from accounts.forms import CustomUserChangeForm, CustomCreationForm


# Register your models here.
@admin.register(UserModel)
class AppUserAdmin(UserAdmin):

    form = CustomUserChangeForm
    add_form = CustomCreationForm

    list_display = ('username', 'email')

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )

    fieldsets = (
        ('Credentials', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login',)})
    )