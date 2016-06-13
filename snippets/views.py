from django.shortcuts import render, get_object_or_404
from django.http import Http404
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
#Class-Based views

class SnippetList(APIView):
	permission_classes = (IsAuthenticated,)
	#List all snippets or create a new snippet
	def get(self, request, format=None):
		snippets = Snippet.objects.all()
		serializer = SnippetSerializer(snippets, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = SnippetSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
	permission_classes = (IsAuthenticated,)
	#Retrieve, update or delete a snippet instance.
	def get_object(self, pk):
		return get_object_or_404(Snippet, pk=pk)

	def get(self, request, pk, format=None):
		snippet = self.get_object(pk)
		serializer = SnippetSerializer(snippet)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		snippet=self.get_object(pk)
		serializer = SnippetSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		snippet = get_object(pk)
		snippet.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)








#Response object
# REST framework introduces a Response object, which is a type of TemplateResponse that takes unrendered content and uses content negotiation to determine the 
# correct content type to return to the client.
# return Response(data)  # Renders to content type as requested by the client.

#Wrappers
# The @api_view decorator for working with function based views.
# The APIView class for working with class based views

#////////////////////////////////////////////////////////////////////////////////////////////
# class JSONResponse(HttpResponse):
# 	#HttpResponse that renders its content into json.
# 	def __init__(self, data, **kwargs):
# 		content = JSONRenderer().render(data)
# 		kwargs['content_type'] = 'application/json'
# 		super(JSONResponse, self).__init__(content, **kwargs)

	# There are two typical use cases for super. In a class hierarchy with single inheritance, super can be used to refer to parent classes without naming them explicitly,
	# thus making the code more maintainable. This use closely parallels the use of super in other programming languages.
	# The second use case is to support cooperative multiple inheritance in a dynamic execution environment. This use case is unique to Python and is not found in 
	# statically compiled languages or languages that only support single inheritance. This makes it possible to implement “diamond diagrams” where multiple base 
	# classes implement the same method. Good design dictates that this method have the same calling signature in every case (because the order of calls is
	# determined at runtime, because that order adapts to changes in the class hierarchy, and because that order can include sibling classes that are unknown prior to runtime).
	
	#class C(B):
 	#	def method(self, arg):
 	#		super(C, self).method(arg)

#Function-Based views
#////////////////////////////////////////////////////////////////////////////////
# @csrf_exempt
# @api_view(['GET', 'POST'])
# @permission_classes((permissions.AllowAny,))
# def snippet_list(request, format=None):
# 	#To list all code snippets, or create a new snippet
# 	if request.method == 'GET':
# 		snippets = Snippet.objects.all()
# 		serializer = SnippetSerializer(snippets, many=True)
# 		return Response(serializer.data)
# 	#Note that because we want to be able to POST to this view from clients that won't have a CSRF token we need to mark the view as csrf_exempt
	
# 	# REST framework introduces a Request object that extends the regular HttpRequest, and provides more flexible request parsing. The core functionality of the Request 
# 	# object is the request.data attribute, which is similar to request.POST, but more useful for working with Web APIs.

# 	# request.POST  # Only handles form data.  Only works for 'POST' method.
# 	# request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.
# 	elif request.method == 'POST':
# 		serializer = SnippetSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# view which corresponds to an individual snippet, and can be used to retrieve, update or delete the snippet.
# @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((permissions.AllowAny,))
# def snippet_detail(request, pk, format=None):
# 	# try:
#  #        snippet = Snippet.objects.get(pk=pk)
#  #    except Snippet.DoesNotExist:
#  #        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
# 	snippet = get_object_or_404(Snippet, pk=pk)
# 	if request.method == 'GET':
# 		serializer = SnippetSerializer(snippet)
# 		return Response(serializer.data)

# 	elif request.method == 'PUT':
# 		#data = JSONParser().parse(request)
# 		serializer = SnippetSerializer(snippet, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	elif request.method == 'DELETE':
# 		snippet.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)

# # we're no longer explicitly tying our requests or responses to a given content type. request.data can handle incoming json requests, but it can also handle other formats. 
# # Similarly we're returning response objects with data, but allowing REST framework to render the response into the correct content type for us.