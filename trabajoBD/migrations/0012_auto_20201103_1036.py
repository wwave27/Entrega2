# Generated by Django 3.1.2 on 2020-11-03 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajoBD', '0011_auto_20201103_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
