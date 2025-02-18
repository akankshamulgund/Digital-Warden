# Generated by Django 5.0.3 on 2024-03-09 13:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_auto_20200522_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlockedAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(max_length=100)),
                ('reporter_name', models.CharField(max_length=100)),
                ('reason', models.TextField()),
            ],
            options={
                'verbose_name': 'Blocked Account',
                'verbose_name_plural': 'Blocked Accounts',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.account')),
            ],
        ),
    ]
