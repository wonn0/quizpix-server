from quizpix.models import CustomUser, Quiz, Question, Item
from quizpix.serializers import UserSerializer, QuizSerializer, QuestionSerializer, ItemSerializer

from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.hashers import make_password, check_password

#filtering
from django_filters.rest_framework import DjangoFilterBackend



# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username']

    def update(self, request, *args, **kwargs):
        # hash the password if it is being updated
        if 'password' in request.data and request.data['password'] != '':
            request.data['password'] = make_password(request.data['password'])
        else:
            request.data.pop('password', None)

        return super().update(request, *args, **kwargs)
    
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