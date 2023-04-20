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
    # once we delete all the null pp users, set null = False, we'll be using blank instead
    profile_picture = models.ImageField(upload_to = 'uploads/', blank = False, null = True)
    status = models.CharField(max_length = 100, choices = STATUS, default = 'regular')
    quizzes_made = models.IntegerField(default = 0)
    total_score = models.IntegerField(default = 0)
    items = ArrayField(
        models.IntegerField(default = 0),
        size = 3,
    )
    
    def __str__(self):
        return self.username

class Quiz(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'uploads/', null = True)
    title = models.CharField(max_length = 255, null = False, blank = False, default = 'My Quiz')
    is_shared = models.BooleanField(default = False)

class Question(models.Model):

    TYPES = (
        ('multiple_choice', 'multiple_choice'),
        ('true_or_false', 'true_or_false'),
        ('identification', 'identification')
    )

    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    type = models.CharField(max_length = 100, choices = TYPES, null = False, blank = False)
    question = models.TextField(null = False, blank = False)
    answer = models.CharField(max_length = 255, null = False, blank = False)
    choices = ArrayField(
        models.CharField(max_length = 255),
        size = 4,
        blank = True, 
        null = False
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

# class Item(models.Model):
    
#     TYPES = (
#         ('bonus', 'bonus'),
#         ('redo', 'redo'),
#         ('free_pass', 'free_pass')
#     )

#     user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
#     quantity = models.IntegerField(default = 0)
#     type = models.CharField(max_length = 100, choices = TYPES, null = False, blank = False)