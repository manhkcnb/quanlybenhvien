# Generated by Django 4.1.13 on 2024-05-29 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
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
        migrations.RemoveField(
            model_name='patient',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='last_name',
        ),
        migrations.AddField(
            model_name='patient',
            name='fullname',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='patient.fullname'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.address'),
        ),
    ]