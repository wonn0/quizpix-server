from quizpix.models import CustomUser, Quiz, Question, Item
from quizpix.serializers import UserSerializer, QuizSerializer, QuestionSerializer, ItemSerializer

from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

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

        # If profile_picture is not included in the request, keep the original profile picture
        if 'profile_picture' not in request.data:
            if self.get_object().profile_picture:
             request.data['profile_picture'] = self.get_object().profile_picture

        return super().update(request, *args, **kwargs)
    
    @action(detail=False, methods=['post'])
    def validate_password(self, request):
        password = request.data.get('password')
        if password:
            user = request.user
            is_valid = check_password(password, user.password)
            return Response({'is_valid': is_valid})
        else:
            return Response({'error': 'Password not provided.'}, status=status.HTTP_400_BAD_REQUEST)
        
class QuizViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'is_shared']

    def update(self, request, *args, **kwargs):
        # If profile_picture is not included in the request, keep the original profile picture
        if 'image' not in request.data:
            if self.get_object().image:
             request.data['image'] = self.get_object().image

        return super().update(request, *args, **kwargs)

class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['quiz']

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