# main_app/models.py

from django.db import models

class ScanResult(models.Model):
    ip_address = models.CharField(max_length=100)
    hostname = models.CharField(max_length=100)
    status = models.CharField(max_length=20)  # e.g., "up" or "down"
    os = models.CharField(max_length=100)
    open_ports = models.TextField()  # Store open ports as a comma-separated string or JSON field

    def __str__(self):
        return f"{self.hostname} ({self.ip_address})"
