# Generated by Django 3.0.2 on 2020-03-12 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0002_auto_20200312_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='composition_file',
            field=models.FileField(default='None', max_length=500, upload_to=''),
        ),
        migrations.AlterField(
            model_name='score',
            name='music_file',
            field=models.FileField(default='None', max_length=10000, upload_to=''),
        ),
        migrations.AlterField(
            model_name='score',
            name='pdf_file',
            field=models.FileField(default='None', max_length=100000, upload_to=''),
        ),
    ]
