# Generated by Django 4.2.11 on 2024-06-07 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_delete_usergeneralinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthPatientHistory',
            fields=[
                ('id', models.PositiveBigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('health_id', models.PositiveBigIntegerField()),
                ('date', models.DateField()),
                ('doctor', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.PositiveBigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('result_id', models.PositiveBigIntegerField()),
                ('value', models.FloatField()),
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
        migrations.CreateModel(
            name='VisitDetails',
            fields=[
                ('id', models.PositiveBigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('details_id', models.PositiveBigIntegerField()),
                ('drugs', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
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
            name='Tests',
            fields=[
                ('id', models.PositiveBigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('test_id', models.PositiveBigIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('doctor', models.CharField(max_length=255)),
                ('order_date', models.DateField()),
                ('executive_date', models.DateField()),
                ('price', models.FloatField()),
                ('results', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.results')),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.PositiveBigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('health_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.healthpatienthistory')),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tests')),
            ],
        ),
        migrations.AddField(
            model_name='healthpatienthistory',
            name='details_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.visitdetails'),
        ),
    ]
