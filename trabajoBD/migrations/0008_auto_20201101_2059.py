# Generated by Django 3.1.2 on 2020-11-01 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajoBD', '0007_auto_20201030_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nintendo',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='pc',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='playstation',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='retro',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='xbox',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
