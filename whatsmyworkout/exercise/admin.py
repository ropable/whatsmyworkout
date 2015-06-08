from django.contrib import admin
from .models import ExerciseCategory, Equipment, Demo, Exercise


@admin.register(ExerciseCategory)
class ExerciseCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Demo)
class DemoAdmin(admin.ModelAdmin):
    pass


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass
