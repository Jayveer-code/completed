from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *


class ImageInline(admin.TabularInline):
    model = images

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ('user', 'gender', 'mobile_no', 'address')

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline]
    list_display = ('username', 'first_name', 'last_name', 'email')
    
# class CustomerAdmin(admin.ModelAdmin):
#      list_display =('username','first_name','last_name','mail','gender','mobile_no','address')      

admin.site.register(images)
# admin.site.register(UserProfile)
admin.site.register(contact_us)
admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Filter_Price)
admin.site.register(Product,ProductAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
# Register your models here.

