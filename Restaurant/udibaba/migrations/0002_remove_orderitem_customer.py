# Generated by Django 4.0.3 on 2022-06-18 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('udibaba', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='customer',
        ),
    ]