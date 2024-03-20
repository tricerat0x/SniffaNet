# Generated by Django 5.0.3 on 2024-03-19 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=100)),
                ('mac_address', models.CharField(max_length=100)),
                ('os', models.CharField(max_length=100)),
                ('open_ports', models.TextField()),
            ],
        ),
    ]
