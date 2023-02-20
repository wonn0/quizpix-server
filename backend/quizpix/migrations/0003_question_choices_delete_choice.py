# Generated by Django 4.1.5 on 2023-01-03 08:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizpix', '0002_customuser_profile_picture_customuser_title_quiz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='choices',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255, null=True), default=[], size=3),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
