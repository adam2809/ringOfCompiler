# Generated by Django 2.1.2 on 2018-11-24 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20181124_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='input',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='test',
            name='output',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='test',
            name='task',
            field=models.IntegerField(default=0),
        ),
    ]