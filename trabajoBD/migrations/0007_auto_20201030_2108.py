# Generated by Django 3.1.2 on 2020-10-31 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajoBD', '0006_auto_20201030_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lanzamientos',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='tags',
            name='sigla2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
