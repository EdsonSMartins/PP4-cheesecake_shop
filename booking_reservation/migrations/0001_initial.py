# Generated by Django 5.0.4 on 2024-05-03 12:29

import datetime
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone', models.CharField(blank=True, max_length=30)),
                ('number_of_guests', models.IntegerField(default=2)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('reservation_date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date.today)])),
                ('reservation_time', models.TimeField(default=django.utils.timezone.now)),
                ('notes', models.TextField(blank=True, max_length=300, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Booked', 'Booked')], default='Pending', max_length=10)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
