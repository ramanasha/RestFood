# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 19:26
from __future__ import unicode_literals

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Foodie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Foodie_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[(b'm', b'Male'), (b'f', b'Female'), (b'u', b'Undenifed')], max_length=1)),
                ('city', models.CharField(choices=[(b'zulia', b'Zulia'), (b'caracas', b'Caracas'), (b'valencia', b'Valencia'), (b'barquisimeto', b'Barquisimeto'), (b'maracay', b'Maracay'), (b' ciudad guayana', b' Ciudad Guayana'), (b'san cristobal', b'San Cristobal'), (b'barcelona', b'Barcelona'), (b'maturin', b'Maturin'), (b'ciudad bolivar', b'Ciudad Bolivar'), (b'puerto la cruz', b'Puerto La Cruz'), (b'merida', b'Merida'), (b'punto fijo', b'Punto Fijo'), (b'los teques', b'Los Teques'), (b'acarigua', b'Acarigua'), (b'carabobo', b'Carabobo'), (b'valera', b'Valera'), (b'apure', b'Apure'), (b'coro', b'Coro'), (b'puerto cabello', b'Puerto Cabello')], default='caracas', max_length=15)),
                ('avatar', models.ImageField(default='user_profile/default.jpg', upload_to='user_profile/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('foodie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='foodie.Foodie')),
            ],
        ),
        migrations.CreateModel(
            name='RelationShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follows', models.ManyToManyField(related_name='followed_by', to='foodie.RelationShip')),
                ('user', core.models.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, to='foodie.Foodie')),
            ],
        ),
    ]
