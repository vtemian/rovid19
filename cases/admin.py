from django.contrib import admin
from .models import Cases


@admin.register(Cases)
class CasesAdmin(admin.ModelAdmin):
    pass
