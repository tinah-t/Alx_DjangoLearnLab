# from django.contrib import admin

# # Register your models here.
# from .models import Book

# class BookAdmin(admin.ModelAdmin):
#     list_filter = ('title', 'author', 'publication_year')
#     search_fields = ('title', 'author')

# admin.site.register(Book , BookAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields visible in admin list
    list_display = ("username", "email", "date_of_birth", "is_staff")

    # Fields visible when editing a user
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

    # Fields visible when creating a user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {
            "fields": ("date_of_birth", "profile_photo"),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
