# Generated by Django 3.0.2 on 2020-03-12 13:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20200303_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('scoreID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('score_file', models.FileField(max_length=300, upload_to='')),
                ('composition_file', models.FileField(default='None', max_length=300, upload_to=' ')),
                ('music_file', models.FileField(default='None', max_length=10000, upload_to=' ')),
                ('pdf_file', models.FileField(default='None', max_length=10000000, upload_to=' ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
    ]
