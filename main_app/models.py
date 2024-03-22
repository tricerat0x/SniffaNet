from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class ScanResult(models.Model):
    STATUS_CHOICES = (
        ('up', 'Up'),
        ('down', 'Down'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)  # Link to the User model
    ip_address = models.CharField(max_length=100)
    hostname = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)  #"up" or "down"
    os = models.CharField(max_length=100)
    open_ports = models.TextField()  # Store open ports as a comma-separated string or JSON field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.hostname} ({self.ip_address})"

class Report(models.Model):
    scan_result = models.ForeignKey(ScanResult, on_delete=models.CASCADE, related_name='reports')
    ip_address = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=50)
    device_type = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.device_type} at {self.ip_address}"
    
    