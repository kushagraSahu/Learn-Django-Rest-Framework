from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import snippets
from snippets.serializers import SnippetSerializer

class JSONResponse(HttpResponse):
	#HttpResponse that renders its content into json.

	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

	# There are two typical use cases for super. In a class hierarchy with single inheritance, super can be used to refer to parent classes without naming them explicitly,
	# thus making the code more maintainable. This use closely parallels the use of super in other programming languages.
	# The second use case is to support cooperative multiple inheritance in a dynamic execution environment. This use case is unique to Python and is not found in 
	# statically compiled languages or languages that only support single inheritance. This makes it possible to implement “diamond diagrams” where multiple base 
	# classes implement the same method. Good design dictates that this method have the same calling signature in every case (because the order of calls is
	# determined at runtime, because that order adapts to changes in the class hierarchy, and because that order can include sibling classes that are unknown prior to runtime).
	
	#class C(B):
 	#	def method(self, arg):
 	#		super(C, self).method(arg)

# Create your views here.

@csrf_exempt
def snippet_list(request):
	#To list all code snippets, or create a new snippet
	if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JSONResponse(serializer.data)
	#Note that because we want to be able to POST to this view from clients that won't have a CSRF token we need to mark the view as csrf_exempt
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

