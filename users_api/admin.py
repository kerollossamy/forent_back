from django.contrib import admin
from users_api.models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role')
    search_fields = ['username','role']
    list_filter = ['registration_date']

	
    
admin.site.register(User,UserAdmin)
