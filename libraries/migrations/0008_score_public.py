# Generated by Django 3.0.2 on 2020-04-04 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0007_auto_20200314_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]