# Generated by Django 3.1.14 on 2024-02-21 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_auto_20240221_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fireteam',
            name='members',
        ),
        migrations.AddField(
            model_name='fireteam',
            name='members',
            field=models.JSONField(default=list),
        ),
    ]
