from quizpix.models import CustomUser, Quiz, Question, Game, Item
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url', 'username', 'password', 'email', 'title']
        # extra_kwargs = {'password': {'write_only': True}}

class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ['url', 'user', 'image', 'title']

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['url', 'quiz', 'type', 'question', 'answer', 'choices']

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['url', 'quiz', 'difficulty']

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['url', 'user', 'type']