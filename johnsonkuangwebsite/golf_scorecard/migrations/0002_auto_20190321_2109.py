# Generated by Django 2.1.3 on 2019-03-22 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('golf_scorecard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scores',
            name='player',
        ),
        migrations.RemoveField(
            model_name='holes',
            name='scores',
        ),
        migrations.DeleteModel(
            name='Scores',
        ),
    ]