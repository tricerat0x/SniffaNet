from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Scan(models.Model):
    pass

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
# User profile extended
class User_Report(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
class Report(models.Model):
    device_id = models.AutoField(primary_key=True)
    scan = models.ForeignKey(Scan, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=50)
    device_type = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    def __str__(self):
        return f"Report {self.device_id}"
    

class Vulnerability(models.Model):
    vulnerability_id = models.AutoField(primary_key=True)
    scan = models.ForeignKey(Scan, on_delete=models.CASCADE)
    device = models.ForeignKey(Report, on_delete=models.CASCADE)
    vulnerability_type = models.CharField(max_length=100)
    severity = models.CharField(max_length=50)
    details = models.TextField()

    def __str__(self):
        return f"Vulnerability {self.vulnerability_id} - {self.vulnerability_type}"






# REPORT = NETWORKDEVICE ERD