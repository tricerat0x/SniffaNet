from django.contrib import admin
from .models import ScanResult
class ScanResultAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user_id = request.user.id
        super().save_model(request, obj, form, change)

admin.site.register(ScanResult, ScanResultAdmin)
