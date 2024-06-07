from rest_framework import generics

from .models import CustomUser
from .serializers import CustomUserSerializer, UserRegistrationSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserRegistrationSerializer
        return CustomUserSerializer
