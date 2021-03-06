# Generated by Django 2.2.10 on 2021-10-01 09:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('user_id', models.IntegerField()),
                ('like', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Users1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('cell_phone', models.CharField(max_length=10)),
                ('is_admin', models.IntegerField(choices=[(0, 'is not admin'), (1, 'is admin user')], default=0)),
                ('password', models.CharField(max_length=50, null=True)),
                ('last_login', models.DateTimeField(default=datetime.datetime(2021, 10, 1, 9, 59, 7, 759508))),
            ],
        ),
    ]
