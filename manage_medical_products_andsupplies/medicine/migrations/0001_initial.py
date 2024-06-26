# Generated by Django 4.1.13 on 2024-05-30 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.IntegerField()),
                ('expiration_date', models.DateField()),
                ('manufacturer', models.CharField(blank=True, max_length=255, null=True)),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('batch_number', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
