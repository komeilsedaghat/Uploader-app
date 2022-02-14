# Generated by Django 4.0 on 2022-02-11 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_imagemodel_videomodel_delete_filemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='file',
            field=models.ImageField(upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='videomodel',
            name='file',
            field=models.FileField(upload_to='video/'),
        ),
    ]