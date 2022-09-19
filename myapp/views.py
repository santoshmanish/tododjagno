from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskManagerSerializer 
from .models import TaskManager
# Create your views here.


@api_view(['GET'])
def api_overview(request):
    all_apis = {
        "add-task": "/add-task",
        "update-task": "/update-task/pk",
        "delete-task": "/del-task/pk",
        "get-task": "/get-task?pk=1"
    }
    return Response(all_apis)

@api_view(['POST'])
def create_task(request):
    task = TaskManagerSerializer(data=request.data)
    if task.is_valid():
        task.save()
        return Response(status=201, data=task.data)
    return Response(status=500)

@api_view(['POST'])
def update_task(request, pk):
    task = TaskManager.objects.get(pk=pk)
    task_seri = TaskManagerSerializer(data=request.data,instance=task)
    if task_seri.is_valid():
        task_seri.save()
        return Response(status=200, data=task_seri.data)
    return Response(status=404, data={'message': 'not found'})

@api_view(['DELETE'])
def delete_task(request, pk):
    TaskManager.objects.filter(pk=pk).delete()
    is_exists = len(TaskManager.objects.filter(pk=pk))
    print(is_exists)
    if not is_exists:
        return Response(data={'message': f'item deleted with id pk'})
    return Response(status=500, data={'message': 'item not deleted'})

@api_view(['GET'])
def get_task(request):
    item = request.query_params.get('param1')    
    if item is not None:
        tasks = TaskManager.objects.filter(pk=item)
    else: 
        tasks = TaskManager.objects.all()
    tasks_data = TaskManagerSerializer(tasks, many=True)
    return Response(status=200, data=tasks_data.data)