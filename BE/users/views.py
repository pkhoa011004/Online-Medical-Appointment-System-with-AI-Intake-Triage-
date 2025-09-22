from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

def user_detail(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'users/user_detail.html', {'user': user})