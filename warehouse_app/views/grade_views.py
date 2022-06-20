from rest_framework import status
from rest_framework.response import Response

from ..models import Grade
from ..serializers import GradeSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def grade_list(request, format=None):
    if request.method == "GET":
        grades = Grade.objects.all()
        serializer = GradeSerializer(grades, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def grade_detail(request, id, format=None):
    try:
        grade = Grade.objects.get(pk=id)
    except Grade.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GradeSerializer(grade)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GradeSerializer(grade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        grade.delete()
        Response(status=status.HTTP_204_NO_CONTENT)
