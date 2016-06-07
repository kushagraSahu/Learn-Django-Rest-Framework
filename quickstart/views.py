from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer

# Create your views here.
#API endpoint which allows models to be viewed or edited.
#Rather than writing multiple views we're grouping together all the common behaviour into classes called ViewSets
#We can easily break these down into individual views if we need to, but using viewsets keeps the view logic nicely organized as well as being very concise.

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer