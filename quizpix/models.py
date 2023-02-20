from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models

# Custom User (based off of Django's built-in User.)
class CustomUser(AbstractUser):

    STATUS = (
        ('regular', 'regular'),
        ('pro', 'pro'),
        ('admin', 'admin')
    )

    title = models.CharField(max_length = 100, default = 'QuizPix Player', null = False, blank = False)
    email = models.EmailField(unique = True, null = False, blank = False)
    profile_picture = models.CharField(max_length = 255, null = False, blank = True)
    status = models.CharField(max_length = 100, choices = STATUS, default = 'regular')
    quizzes_made = models.IntegerField(default = 0)
    total_score = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.username

class Quiz(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    image = models.CharField(max_length = 255, null = False, blank = True)
    title = models.CharField(max_length = 255, null = False, blank = False, default = 'My Quiz')

class Question(models.Model):

    TYPES = (
        ('multiple_choice', 'multiple_choice'),
        ('true_or_false', 'true_or_false'),
        ('identification', 'identification')
    )

    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    type = models.CharField(max_length = 100, choices = TYPES, null = False, blank = False)
    question = models.CharField(max_length = 255, null = False, blank = False)
    answer = models.CharField(max_length = 255, null = False, blank = False)
    choices = ArrayField(
        models.CharField(max_length = 255, null = True, blank = False),
        size = 3,
    )

# class Game(models.Model):

#     DIFFICULTY_LEVELS = (
#         ('easy', 'easy'),
#         ('medium', 'medium'),
#         ('hard', 'hard')
#     )

#     quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
#     game_score = models.IntegerField(default = 0)
#     difficulty = models.CharField(max_length = 100, choices = DIFFICULTY_LEVELS, default = 'medium', null = False, blank = False)
# REMOVE THIS MODEL

class Item(models.Model):
    
    TYPES = (
        ('bonus', 'bonus'),
        ('redo', 'redo'),
        ('free_pass', 'free_pass')
    )

    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 0)
    type = models.CharField(max_length = 100, choices = TYPES, null = False, blank = False)