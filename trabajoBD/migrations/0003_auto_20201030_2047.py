# Generated by Django 3.1.2 on 2020-10-30 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajoBD', '0002_auto_20201030_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='lanzamientos',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='lanzamientos',
            name='update',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='noticia',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='noticia',
            name='update',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='reviews',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='reviews',
            name='update',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
