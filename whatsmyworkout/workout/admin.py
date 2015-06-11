from django.contrib import admin
from .models import WorkoutUser, Workout, Activity


@admin.register(WorkoutUser)
class WorkoutUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_active']
    date_hierarchy = 'date_joined'


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'sets', 'target_difficulty', 'generated', 'delivered', 'feedback']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'workout', 'exercise', 'reps', ]
