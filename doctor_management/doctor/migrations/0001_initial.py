# Generated by Django 4.1.13 on 2024-05-29 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('numberhouse', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='FullName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('working_hours', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='doctor_images/')),
                ('status', models.CharField(max_length=20)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctor.address')),
                ('fullname', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctor.fullname')),
            ],
        ),
    ]
