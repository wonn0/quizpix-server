# Generated by Django 4.1.7 on 2023-03-16 10:35

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizpix', '0019_alter_question_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='choices',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, size=4),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(),
        ),
    ]