# Generated by Django 3.1 on 2020-08-21 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20200815_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile.png', null=True, upload_to=''),
        ),
    ]
