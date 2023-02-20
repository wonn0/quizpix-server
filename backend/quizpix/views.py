# from django.shortcuts import render
# from django.contrib.auth import login
# from knox import views as knox_views

from quizpix.models import CustomUser, Quiz, Question, Item
from quizpix.serializers import UserSerializer, QuizSerializer, QuestionSerializer, ItemSerializer

from rest_framework import viewsets
# from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.authtoken.serializers import AuthTokenSerializer

# Create your views here.

# class CreateUserAPI(CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CreateUserSerializer
#     permission_classes = [permissions.AllowAny]

# Authentication

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class QuizViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [AllowAny]

class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]

# class GameViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Game.objects.all()
#     serializer_class = GameSerializer
#     permission_classes = [permissions.IsAuthenticated]

class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]