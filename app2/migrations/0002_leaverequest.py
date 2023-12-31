# Generated by Django 4.1.5 on 2023-03-29 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=100)),
                ('leave_type', models.CharField(choices=[('vacation', 'Vacation'), ('sick_leave', 'Sick Leave'), ('personal_leave', 'Personal Leave')], max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('reason', models.TextField()),
            ],
        ),
    ]
