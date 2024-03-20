# Generated by Django 3.1.5 on 2024-03-20 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('device_id', models.AutoField(primary_key=True, serialize=False)),
                ('ip_address', models.CharField(max_length=100)),
                ('mac_address', models.CharField(max_length=50)),
                ('device_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vulnerability',
            fields=[
                ('vulnerability_id', models.AutoField(primary_key=True, serialize=False)),
                ('vulnerability_type', models.CharField(max_length=100)),
                ('severity', models.CharField(max_length=50)),
                ('details', models.TextField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.report')),
                ('scan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.scan')),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='scan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.scan'),
        ),
    ]
