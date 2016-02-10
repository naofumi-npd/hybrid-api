from rest_framework import serializers
from menu.models import Menu

class MenuSerializer(serializers.Serializer):
	
	pk = serializers.IntegerField(read_only=True)
	name = serializers.CharField(max_length=255)
	description = serializers.CharField(max_length=255)
	image = serializers.CharField(max_length=255)


	class Meta:
		model = Menu
		fields = ('id', 'name', 'description', 'image')
