# Generated by Django 2.1.3 on 2019-03-25 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golf_scorecard', '0002_auto_20190321_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='person',
        ),
        migrations.RemoveField(
            model_name='player',
            name='team',
        ),
        migrations.RemoveField(
            model_name='team',
            name='players',
        ),
        migrations.RemoveField(
            model_name='game',
            name='winner',
        ),
        migrations.RemoveField(
            model_name='scorecard',
            name='players',
        ),
        migrations.AddField(
            model_name='holes',
            name='hole_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='holes',
            name='hcp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='holes',
            name='par',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
