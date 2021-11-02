from rest_framework.views import APIView
from rest_framework.response import Response

from django.db.models import Count
from .models import Blog
from .serializers import TopAuthorsSerializer


class TopAuthorsView (APIView):
    def get (self, request):
        top = (Blog.objects
               .values('author')
               .annotate(count=Count('author'))
               .order_by('-count','author')
               )[:10]
        serializer = TopAuthorsSerializer(top, many=True)
        return Response(serializer.data)





