# Generated by Django 4.0.3 on 2022-05-27 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udibaba', '0002_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.CharField(max_length=150),
        ),
    ]
