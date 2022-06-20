from rest_framework import status
from rest_framework.response import Response

from ..models import Bar
from ..serializers import BarSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def bar_list(request, format=None):
    if request.method == "GET":
        bars = Bar.objects.all()
        serializer = BarSerializer(bars, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def bar_detail(request, id, format=None):
    try:
        bar = Bar.objects.get(pk=id)
    except Bar.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BarSerializer(bar)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BarSerializer(bar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bar.delete()
        Response(status=status.HTTP_204_NO_CONTENT)
