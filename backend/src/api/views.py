# from django.shortcuts import get_object_or_404
import datetime
from django.shortcuts import render
from django.http import JsonResponse
from .models import ToDo
import json
from django.views.decorators.csrf import csrf_exempt



def todo_list(request):
    print(request)
    if request.method == "GET":
        todo_obj = ToDo.objects.all()
        objs = []
        for obj in todo_obj:
            objs.append({
                'id': obj.id,
                'name': obj.name,
                'description': obj.description,
                'created_at': obj.created_at
            })
        return JsonResponse({
            "data": objs,
            "status": "OK"
        })
    else:
        return JsonResponse({"status":"BAD_REQUEST"})


@csrf_exempt
def create(request):
    if request.method == "POST":
        try:
            request_data = json.load(request)
            name = request_data.get('name', '')
            description = request_data.get('description', '')
            created_obj = ToDo.objects.create(
                name = name,
                description = description,
                created_at=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            return JsonResponse({"status": "CREATED"})
        except Exception as e:
            return JsonResponse({"error": e })
    else:
        return JsonResponse({"status": "BAD_REQUEST"})


@csrf_exempt
def delete(request, pk):
    if request.method == "POST":
        obj = ToDo.objects.get(pk=pk)
        obj.delete()
        return JsonResponse({
            "status":"DELETED"
        })
    else:
        return JsonResponse({
            "status": "BAD_REQUEST"
        })
