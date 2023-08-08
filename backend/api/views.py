from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ToDoSerializer
from .models import ToDo

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'endpoint':'/todo/',
            'method': 'GET',
            'body': None,
            'description': 'Return someone todo'
        },
        {
            'endpoint':'/todo/id',
            'method': 'GET',
            'body': None,
            'description': 'Return one todo'
        },
        {
            'endpoint':'/todo/create/',
            'method': 'POST',
            'body': {'body': ''},
            'description': 'Create one todo'
        },
        {
            'endpoint':'/todo/id/update/',
            'method': 'PUT',
            'body': {'body': ''},
            'description': 'Update one todo'
        },
        {
            'endpoint':'/todo/id/update/',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete one todo'
        },
        
    ]
    return Response(routes)

@api_view(['GET'])
def getToDos(request):
    todos = ToDo.objects.all()
    serialazer = ToDoSerializer(todos, many=True)
    return Response(serialazer.data)

@api_view(['GET'])
def getToDo(request, pk):
    todo = ToDo.objects.get(id=pk)
    serialazer = ToDoSerializer(todo, many=False)
    return Response(serialazer.data)