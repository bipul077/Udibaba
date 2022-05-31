# Generated by Django 3.2 on 2022-05-27 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udibaba', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='video/')),
                ('caption', models.CharField(max_length=100)),
            ],
        ),
    ]