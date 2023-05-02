from .models import Text
from .serializers import TextSerializer
import uuid
# Django Rest Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

@api_view(['POST'])
def create_text(request):
    serializer = TextSerializer(data=request.data)
    if serializer.is_valid():
        text = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_text(request, url):
    text = get_object_or_404(Text, url=url)
    serializer = TextSerializer(instance=text, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def retrieve_text(request, url):
    text = get_object_or_404(Text, url=url)
    serializer = TextSerializer(text, many=False)
    return Response(serializer.data)


