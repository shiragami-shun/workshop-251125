from django.contrib import admin
from .models import Goal

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'target_date', 'created_at')
    list_filter = ('status', 'category', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('基本情報', {
            'fields': ('title', 'description')
        }),
        ('分類', {
            'fields': ('category', 'status')
        }),
        ('スケジュール', {
            'fields': ('target_date',)
        }),
        ('タイムスタンプ', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
