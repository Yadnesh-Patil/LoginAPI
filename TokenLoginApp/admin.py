from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

admin.site.register(CustomUser, UserAdmin)
class CustomeUserAdmin(admin.ModelAdmin):
    list_display=['username','first_name','last_name','email','age','phone','gender']
