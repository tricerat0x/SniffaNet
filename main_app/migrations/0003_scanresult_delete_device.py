# Generated by Django 5.0.3 on 2024-03-19 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_mac_address_device_hostname'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScanResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=100)),
                ('hostname', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
                ('os', models.CharField(max_length=100)),
                ('open_ports', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Device',
        ),
    ]
