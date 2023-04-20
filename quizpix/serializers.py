from quizpix.models import CustomUser, Quiz, Question
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url', 'username', 'password', 'email', 'title', 'profile_picture', 'is_active', 'quizzes_made', 'total_score', 'status', 'items']
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password) # hash the password using set_password method
        user.save()
        return user

class QuizSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.StringRelatedField(source='user.username', read_only=True)
    class Meta:
        model = Quiz
        fields = ['url', 'user', 'username', 'image', 'title', 'is_shared',]

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['url', 'quiz', 'type', 'question', 'answer', 'choices']

# class GameSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Game
#         fields = ['url', 'quiz', 'difficulty']
