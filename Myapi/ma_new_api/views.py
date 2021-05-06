from django.shortcuts import render
#from django.http import HttpResponse
#from django.shortcuts import get_object_or_404
#from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import viewsets
#from rest_framework.response import Response
#from rest_framework import status
from .serializer import UserSerializer,AdminSerializer,BookcallsSerializer
from .models import Admin,Book_calls,User
# Create your views here.

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookCallsViewSet(viewsets.ModelViewSet):
    queryset = Book_calls.objects.all()
    serializer_class = BookcallsSerializer
    permission_classes = [permissions.IsAuthenticated]