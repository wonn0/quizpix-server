# Generated by Django 4.1.7 on 2023-02-25 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizpix', '0012_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='', upload_to='uploads/'),
        ),
    ]
