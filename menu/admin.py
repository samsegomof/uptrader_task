from django.contrib import admin

from menu.models import MenuElement


@admin.register(MenuElement)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'parent']
    list_editable = ['name', 'slug', 'parent']
    mptt_level_indent = 20

