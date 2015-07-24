# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	
	list_display = ('username','first_name','last_name')
	fieldsets = (
		('User',{'fields': ('username','password')}),
		('Personal Info',{'fields': ('first_name','last_name')}),
	)
