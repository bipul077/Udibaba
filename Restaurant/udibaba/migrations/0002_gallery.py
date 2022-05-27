# Generated by Django 4.0.3 on 2022-05-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udibaba', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(default=False, max_length=50)),
                ('image', models.ImageField(default='default.jpg', upload_to='gallery_imgs/')),
            ],
        ),
    ]
