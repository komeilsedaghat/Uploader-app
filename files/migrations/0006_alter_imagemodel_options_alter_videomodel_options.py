# Generated by Django 4.0 on 2022-02-14 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_alter_imagemodel_options_alter_videomodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagemodel',
            options={'ordering': ['-time']},
        ),
        migrations.AlterModelOptions(
            name='videomodel',
            options={'ordering': ['-time']},
        ),
    ]
