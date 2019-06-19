from django.contrib import admin
from .models import Banks, Branches

@admin.register(Banks)
class BankAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('name', )

@admin.register(Branches)
class BranchesAdmin(admin.ModelAdmin):
    list_display = (
        'branch', 'bank', 'city', 'district',
    )
    search_fields = ('bank', 'city')
    list_filter = ('bank',)