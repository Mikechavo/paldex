# Generated by Django 4.2.9 on 2024-02-23 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_alter_fireteam_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fireteam',
            name='members',
        ),
        migrations.AddField(
            model_name='fireteam',
            name='members',
            field=models.JSONField(default=dict),
        ),
    ]
