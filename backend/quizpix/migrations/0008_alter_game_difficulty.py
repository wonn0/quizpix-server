# Generated by Django 4.1.5 on 2023-01-03 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizpix', '0007_alter_question_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='difficulty',
            field=models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')], default='medium', max_length=100),
        ),
    ]
