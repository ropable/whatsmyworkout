from django.contrib import admin
from .models import ExerciseCategory, Equipment, Demo, Exercise


@admin.register(ExerciseCategory)
class ExerciseCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Demo)
class DemoAdmin(admin.ModelAdmin):
    list_display = ['url', '__str__']
    search_fields = ['url', 'description']


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'difficulty', 'categories_display', 'equipment_display',
        'demos_display']
    list_filter = ['difficulty', 'equipment_req', 'categories']
    search_fields = ['name', 'difficulty', 'categories__name', 'equipment_req__name']

    def categories_display(self, obj):
        return ', '.join([c.name for c in obj.categories.all()])
    categories_display.short_description = 'Categories'

    def equipment_display(self, obj):
        return ', '.join([e.name for e in obj.equipment_req.all()])
    equipment_display.short_description = 'Equipment'

    def demos_display(self, obj):
        return obj.demos.count()
    demos_display.short_description = 'Demos count'
