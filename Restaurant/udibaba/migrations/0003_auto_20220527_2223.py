# Generated by Django 3.2 on 2022-05-27 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udibaba', '0002_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video',
        ),
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(default='mama', max_length=100),
            preserve_default=False,
        ),
    ]