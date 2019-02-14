from django.contrib import admin
from .models import Profile


class ProfileItemInline(admin.TabularInline):
    model = Profile
    raw_id_fields = ['movie']


class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'city', 'postcode', 'date_birth', 'preferred_genre']


admin.site.register(Profile, UserAdmin)
