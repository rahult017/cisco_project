from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated  # <-- Here
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import *
from rest_framework import generics

class RouterCreateApi(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Router_Details.objects.all()
    serializer_class = RouterSerializer

class RouterApi(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Router_Details.objects.all()
    serializer_class = RouterSerializer

class RouterDetails(APIView):
    permission_classes = (IsAuthenticated,)
    def post(request,loopback):
        queryset = Router_Details.objects.get(Loopback=loopback)
        data = request.data
        serializer = RouterSerializer(queryset,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        querset = Router_Details.objects.filter(id=id).update(is_delete=True)
        router = Router_Details.objects.filter(is_delete=False)
        serializer = RouterSerializer(router,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    
class Routerfilter(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        first_ip = request.POST.get('ip')
        second_ip = request.POST.get('ipaddress')
        querset = Router_Details.objects.filter(Loopback__lte=second_ip,Loopback__gte=first_ip)
        serializer = RouterSerializer(querset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
