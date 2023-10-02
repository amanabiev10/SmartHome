from django.contrib import admin
from .models import Lamp, LampStatistics


@admin.register(Lamp)
class LampAdmin(admin.ModelAdmin):
    pass


@admin.register(LampStatistics)
class LampStatisticsAdmin(admin.ModelAdmin):
    pass