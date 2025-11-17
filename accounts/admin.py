from django.contrib import admin
from .models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	list_display_links = ('user','first_name')
	list_display = ('user', 'first_name', 'last_name', 'phone_number', 'address', 'created_at', 'updated_at')
	search_fields = ('user__username', 'first_name', 'last_name', 'phone_number')

admin.site.register(Profile, ProfileAdmin)

