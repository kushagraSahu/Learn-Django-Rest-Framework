from snippets.models import Snippet
from django.contrib.auth.models import User
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

#Creating single entry point to the API.
@api_view(['GET'])
def api_root(request, format=None):	
	return Response({
			'users': reverse('user-list', request=request, format=format),
			'snippets': reverse('snippet-list', request=request, format=format)
		})

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

#There are two styles of HTML renderer provided by REST framework, one for dealing with HTML rendered using templates, the other for dealing with pre-rendered HTML. 
#The second renderer is the one we'd like to use for this endpoint.
class SnippetHighlight(generics.GenericAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )

	queryset = Snippet.objects.all()
	renderer_classes = (renderers.StaticHTMLRenderer, )
#Since there's no existing generic view which we can use to return property of object instance, we have to use base class for representing instances, and create our own .get() method.
	def get(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)