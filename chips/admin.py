from django.contrib import admin
from . import models


@admin.register(models.Chip)
class ChipAdmin(admin.ModelAdmin):
    pass
