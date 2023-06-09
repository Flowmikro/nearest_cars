# Generated by Django 4.2.1 on 2023-05-23 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('state_name', models.CharField(max_length=255)),
                ('zip', models.PositiveSmallIntegerField()),
                ('lat', models.DecimalField(decimal_places=35, max_digits=35)),
                ('lng', models.DecimalField(decimal_places=35, max_digits=35)),
            ],
        ),
    ]
