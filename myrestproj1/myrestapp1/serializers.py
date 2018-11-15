from rest_framework import serializers
class CommentSerializer(serializers.Serializer):
	email=serializers.EmailField()
	content=serializers.CharField(max_length=30)
	created=serializers.DateTimeField()