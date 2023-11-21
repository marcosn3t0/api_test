from django.http import JsonResponse
from .models import Vape
from .serializers import VapeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def vape_list(request,format=None):

    if request.method=='GET':
        vapes = Vape.objects.all()
        serializer = VapeSerializer(vapes, many=True)
        return JsonResponse({'vapes':serializer.data})
    
    elif request.method == 'POST':
        serializer = VapeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def vape_detail(request,id,format=None):

    try:
        vape = Vape.objects.get(id=id)
    except Vape.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = VapeSerializer(vape)
        return JsonResponse(serializer.data)
    
    elif request.method == 'POST':
        serializer = VapeSerializer(vape,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        vape.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        