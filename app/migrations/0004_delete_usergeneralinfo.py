# Generated by Django 4.2.11 on 2024-06-07 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_usergeneralinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserGeneralInfo',
        ),
    ]