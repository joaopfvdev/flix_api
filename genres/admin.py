from django.contrib import admin
from genres.models import Genre


@admin.register(Genre)
class Genreadmim(admin.ModelAdmin):
    list_display = ('id', 'name',)
