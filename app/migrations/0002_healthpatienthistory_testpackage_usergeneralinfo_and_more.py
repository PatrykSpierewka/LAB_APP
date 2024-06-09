# Generated by Django 4.2.11 on 2024-06-09 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthPatientHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('health_id', models.PositiveBigIntegerField(blank=True, null=True)),
                ('date', models.DateField()),
                ('doctor', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TestPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserGeneralInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='blood_test_doctor',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='x_ray_doctor',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('gender', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('health_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.healthpatienthistory')),
            ],
        ),
    ]
