# Generated by Django 4.1.7 on 2023-03-09 14:03

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizpix', '0018_alter_question_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='choices',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, default=[], size=3),
            preserve_default=False,
        ),
    ]
