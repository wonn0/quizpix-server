# Generated by Django 4.1.7 on 2023-02-25 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizpix', '0011_alter_customuser_profile_picture_alter_quiz_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
