# Generated by Django 4.0 on 2022-02-14 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='TwoFactorAuthentication',
            field=models.BooleanField(default=False),
        ),
    ]