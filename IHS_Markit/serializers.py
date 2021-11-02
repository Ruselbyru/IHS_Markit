from rest_framework import serializers



class TopAuthorsSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=30)
    count = serializers.IntegerField()