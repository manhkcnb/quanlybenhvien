# Generated by Django 4.1.13 on 2024-06-01 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_remove_doctor_department_doctor_department_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='Department',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='department_id',
        ),
        migrations.AddField(
            model_name='department',
            name='department_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='department',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='doctor.department'),
            preserve_default=False,
        ),
    ]