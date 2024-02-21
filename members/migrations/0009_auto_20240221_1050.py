# Generated by Django 3.1.14 on 2024-02-21 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paldex', '0010_auto_20240221_0731'),
        ('members', '0008_auto_20240221_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fireteam',
            name='members',
            field=models.ManyToManyField(default=list, related_name='fire_teams_joined', to='paldex.PalModel'),
        ),
    ]
