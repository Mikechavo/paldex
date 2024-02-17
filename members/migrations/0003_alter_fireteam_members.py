# Generated by Django 5.0.1 on 2024-02-17 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_delete_pal'),
        ('paldex', '0007_alter_palmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fireteam',
            name='members',
            field=models.ManyToManyField(related_name='fire_teams_joined', to='paldex.palmodel'),
        ),
    ]
