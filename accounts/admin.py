from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreateForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'age', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields":('age',)}),
    )
    add_fieldsets = UserAdmin.fieldsets + (
        (None, {"fields":('age',)}),
    )
    


admin.site.register(CustomUser, CustomUserAdmin)
