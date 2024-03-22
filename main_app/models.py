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
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)  # e.g., "up" or "down"
    os = models.CharField(max_length=100)
    open_ports = models.TextField()  # Store open ports as a comma-separated string or JSON field

    def __str__(self):
        return f"{self.hostname} ({self.ip_address})"

    def save(self, *args, **kwargs):
        # Set the user field to the current logged-in user if available
        if not self.user_id:
            user_model = get_user_model()
            user = kwargs.pop('user', None)
            if user and isinstance(user, user_model):
                self.user = user
        super().save(*args, **kwargs)

class Report(models.Model):
    device_id = models.AutoField(primary_key=True)
    scan = models.ForeignKey(Scan, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=50)
    device_type = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report {self.device_id}"
    
    