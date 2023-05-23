# Generated by Django 4.2.1 on 2023-05-23 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='truck',
            name='number',
        ),
        migrations.AddField(
            model_name='truck',
            name='sku',
            field=models.CharField(blank=True, max_length=5, unique=True),
        ),
    ]