# Generated by Django 2.1.2 on 2018-11-24 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='input',
        ),
        migrations.RemoveField(
            model_name='task',
            name='output',
        ),
    ]
