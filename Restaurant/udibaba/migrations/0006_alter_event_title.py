# Generated by Django 4.0.3 on 2022-06-20 07:33
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udibaba', '0005_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
