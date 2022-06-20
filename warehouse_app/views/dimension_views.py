from rest_framework import status
from rest_framework.response import Response

from ..models import Dimension
from ..serializers import DimensionSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def dimension_list(request, format=None):
    if request.method == "GET":
        dimensions = Dimension.objects.all()
        serializer = DimensionSerializer(dimensions, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DimensionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def dimension_detail(request, id, format=None):
    try:
        dimension = Dimension.objects.get(pk=id)
    except Dimension.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DimensionSerializer(dimension)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DimensionSerializer(dimension, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        dimension.delete()
        Response(status=status.HTTP_204_NO_CONTENT)