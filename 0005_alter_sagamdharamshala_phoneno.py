# Generated by Django 5.0.6 on 2024-09-11 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sagamdharamshala', '0004_alter_sagamdharamshala_phoneno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sagamdharamshala',
            name='phoneno',
            field=models.IntegerField(),
        ),
    ]
