import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .models import User

# Create your views here.
def users(request: HttpResponse) -> HttpResponse:
    if request.method == 'GET':
        users = User.objects.all()
        serialized_users = [user.name for user in users]
        return HttpResponse(json.dumps(serialized_users))
    if request.method == 'POST':
        body = json.loads(request.body)
        user = User(name = body['name'], email = body['email'], age = body['age'])
        user.save()
        return HttpResponse(json.dumps({'id':user.id, 'name': user.name}))
    # Here json.dumps() returns as list.
    # (env) PS C:\Users\91703\OneDrive\Desktop\django-proj\first-django-app> python   
    # Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
    # Type "help", "copyright", "credits" or "license" for more information.
    # >>> import json
    # >>> li = [1,2,3]
    # >>> json.dumps(li)
    # '[1, 2, 3]'
    # >>> out = json.dumps(li)
    # >>> type(out)
    # <class 'str'>
    # json.loads(out)
    # [1, 2, 3]

