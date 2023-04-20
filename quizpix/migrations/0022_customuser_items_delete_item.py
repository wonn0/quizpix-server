# Generated by Django 4.1.7 on 2023-04-20 03:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizpix', '0021_quiz_is_shared'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='items',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=[0, 0, 0], size=3),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
