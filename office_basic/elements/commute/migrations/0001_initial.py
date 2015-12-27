# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 08:01
from __future__ import unicode_literals

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PickUpEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=('base.event',),
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_primary', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('end_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='end_routes', to='base.Place')),
                ('start_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='begin_routes', to='base.Place')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RouteLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(blank=True, help_text='License number of vehicle, eg: DL 01 C AA 1111', max_length=20, validators=[django.core.validators.RegexValidator(code='Invalid Value', message='Invalid License Plate Number [use capital letters only]', regex='^[A-Z]{2}[ -][0-9]{1,2}(?: [A-Z])?(?: [A-Z]*)? [0-9]{4}$')])),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Scooter'), (2, 'Bike'), (3, 'Car'), (4, 'Other Type')], default=3, help_text='Own Private Vehicle Type used for commuting')),
            ],
        ),
        migrations.CreateModel(
            name='CommuteUser',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('base.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='owner',
            field=models.ForeignKey(help_text='Owner of vehicle', on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='commute.CommuteUser'),
        ),
        migrations.AddField(
            model_name='routelog',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='managed_route_logs', to='commute.CommuteUser'),
        ),
        migrations.AddField(
            model_name='routelog',
            name='passengers',
            field=models.ManyToManyField(related_name='passenger_route_logs', to='commute.CommuteUser'),
        ),
        migrations.AddField(
            model_name='routelog',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='commute.Route'),
        ),
        migrations.AddField(
            model_name='route',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes', to='commute.CommuteUser'),
        ),
        migrations.AddField(
            model_name='pickupevent',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pickup', to='commute.RouteLog'),
        ),
    ]
