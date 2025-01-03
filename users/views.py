from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from uuid import uuid4
import uuid

users = {}
@api_view(['GET'])
def read(request,user_id):
    if user_id not in users:
        return Response({"message" : "user doesn't exist"}, status = status.HTTP_404_NOT_FOUND)
    return Response(users[user_id], status = status.HTTP_200_OK)
@api_view(['PUT'])
def update(request,user_id):
    if user_id not in users:
        return Response({"message" : "user doesn't exist"}, status = status.HTTP_404_NOT_FOUND)

    data = request.data
    if 'name' not in data or 'email' not in data or 'age' not in data:
        return Response({"message" : "invalid data"}, status = status.HTTP_400_BAD_REQUEST)
    users[user_id].update({
        'name' : data['name'],
        'email': data['email'],
        'age' : data['age']
    })
    return Response(users[user_id], status = status.HTTP_200_OK)
@api_view(['DELETE'])
def delete(request,user_id):
    if user_id not in users:
        return Response({"message" : "user doesn't exist"}, status = status.HTTP_404_NOT_FOUND)
    del users[user_id]
    return Response("successfuly deleted", status = status.HTTP_200_OK)

@api_view(['GET'])
def userlist(request):
    return Response(users, status = status.HTTP_200_OK)

@api_view(['POST'])
def create(request):
    user_id = str(uuid.uuid4())
    data = request.data
   
    users[user_id] = {
        'id': user_id,  
        'name': data['name'],
        'email': data['email'],
        'age': data['age']
    }
    return Response(users[user_id], status=status.HTTP_201_CREATED)
