from django.shortcuts import render
import json

from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    body = request.body
    data  = {}
    try:
        data = json.loads(body)
    except:
        pass

    return JsonResponse(data)