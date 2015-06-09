from django.contrib import admin
from .models import WorkoutUser


@admin.register(WorkoutUser)
class WorkoutUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_active']
    date_hierarchy = 'date_joined'
