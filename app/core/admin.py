from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.


# Custom User Admin
@admin.register(User)
class CustomUser(UserAdmin):
    """custom user admin for user model"""

    ordering = ("id",)

    list_display = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("personal_info", {"fields": ("name",)}),
        ("permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {"fields": ("email", "name", "password1", "password2"), "classes": "wide"},
        ),
    )
