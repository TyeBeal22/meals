# Generated by Django 2.2.12 on 2021-06-11 02:29

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUUIDModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('meal_id', models.IntegerField(default=0)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('guests', models.IntegerField(default=0)),
                ('contact_date', models.DateTimeField(default=datetime.datetime.now)),
                ('delivery_address', models.TextField(blank=True, null=True)),
                ('is_delivery', models.BooleanField(default=True)),
                ('event_date', models.CharField(max_length=100)),
            ],
        ),
    ]
