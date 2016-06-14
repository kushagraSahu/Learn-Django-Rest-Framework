from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

# class SnippetSerializer(serializers.Serializer):
# 	pk = serializers.IntegerField(read_only=True)
# 	title = serializers.CharField(required=False, allow_blank=True, max_length=100)
# 	code = serializers.CharField(style={'base_template':'textarea.html'})
# 	#The {'base_template': 'textarea.html'} flag above is equivalent to using widget=widgets.Textarea on a Django Form class.
# 	linenos = serializers.BooleanField(required=False)
# 	language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
# 	style = serializers.ChoiceField(choices=STYLE_CHOICES,default='friendly')

class SnippetSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	#The source argument controls which attribute is used to populate a field, and can point at any attribute on the serialized instance. It can also take the dotted notation shown
	#above, in which case it will traverse the given attributes.
	#owner = serializers.CharField(source='owner.username', read_only=True)
	class Meta:
		model = Snippet
		fields = ('owner', 'id', 'title', 'code', 'linenos', 'language', 'style')


	#The create() and update() methods define how fully fledged instances are created or modified when calling serializer.save()
	def create(self, validated_data):
		"""
		Create and return a new `Snippet` instance, given the validated data.
		"""
		return Snippet.objects.create(**validated_data)

	def update(self, instance, validated_data):
		"""
	Update and return an existing `Snippet` instance, given the validated data.
		"""
		instance.title = validated_data.get('title', instance.title)
		instance.code = validated_data.get('code', instance.code)
		instance.linenos = validated_data.get('linenos', instance.linenos)
		instance.language = validated_data.get('language', instance.language)
		instance.style = validated_data.get('style', instance.style)
		instance.save()
		return instance

class UserSerializer(serializers.ModelSerializer):
#Because 'snippets' is a reverse relationship on the User model, it will not be included by default when using the ModelSerializer class, so we needed to add an explicit field for it.
	snippets = serializers.PrimaryKeyRelatedField(queryset=Snippet.objects.all(), many=True)
	
	class Meta:
		model = User
		fields = ('id', 'username', 'snippets')
