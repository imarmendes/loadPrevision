from django.contrib import admin
from .models import RoomName, Tue, DemandFactor1, DemandFactor2, Measurements

@admin.register(RoomName)
class RoomNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')
    search_fields = ('name',)
    list_filter = ('type',)
    ordering = ['name']

@admin.register(Tue)
class TueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'power')
    search_fields = ('name',)
    ordering = ['name']

@admin.register(DemandFactor1)
class DemandFactor1Admin(admin.ModelAdmin):
    list_display = ('id', 'min', 'max', 'fd1')
    ordering = ['id']

@admin.register(DemandFactor2)
class DemandFactor2Admin(admin.ModelAdmin):
    list_display = ('id', 'tueNumber', 'fd2')
    ordering = ['id']

@admin.register(Measurements)
class MeasurementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'demand', 'circuitBreaker', 'phase', 'neutral', 'grounding', 'conduit', 'typePhase')
    ordering = ['id']