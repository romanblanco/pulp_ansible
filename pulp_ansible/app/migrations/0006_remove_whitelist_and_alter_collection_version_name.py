# Generated by Django 2.2.4 on 2019-08-02 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ansible', '0005_collectionversion_is_highest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionversion',
            name='name',
            field=models.CharField(editable=False, max_length=64),
        ),
        migrations.RemoveField(
            model_name='collectionremote',
            name='whitelist',
        ),
    ]
