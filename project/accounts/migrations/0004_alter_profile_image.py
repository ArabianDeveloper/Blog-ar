# Generated by Django 3.2.5 on 2021-09-05 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210905_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/mim-logo.png', upload_to='profile'),
        ),
    ]
