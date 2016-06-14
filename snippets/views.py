from snippets.models import Snippet
from django.contrib.auth.models import User
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly

#REST framework provides a set of already mixed-in generic views that we can use.
class SnippetList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
	#IsAuthenticatedOrReadOnly will ensure that authenticated requests get read-write access, and unauthenticated requests get read-only access.
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )

	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer