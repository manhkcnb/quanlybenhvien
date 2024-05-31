# Generated by Django 4.1.13 on 2024-05-30 17:28

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
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hire_date', models.DateField()),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('nationality', models.CharField(max_length=100)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.address')),
                ('fullName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.fullname')),
            ],
        ),
    ]
