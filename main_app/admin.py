from django.contrib import admin
from .models import ScanResult

# Define a custom admin class for ScanResult
class ScanResultAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Assigning ID to the ScanResult being created
        if not obj.id:
            last_scan_result_id = ScanResult.objects.last().id
            obj.id = last_scan_result_id + 1 if last_scan_result_id else 1
        
        # Save the ScanResult
        super().save_model(request, obj, form, change)

# Register the ScanResult model with the custom admin class
admin.site.register(ScanResult, ScanResultAdmin)
