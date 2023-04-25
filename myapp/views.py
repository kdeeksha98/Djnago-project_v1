from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import BookSerializer



# Create your views here.
 
@api_view(['GET'])
def myapp(request):
    Book_objs = Book.objects.all()
    serializer = BookSerializer(Book_objs, many=True)

    return Response({"status" : 200 , "payload" : serializer.data})

@api_view(['POST'])
def post_Book(request):
    data = request.data
    serializer = BookSerializer(data = request.data)
    if not serializer.is_valid():
       print(serializer.errors)
       return Response({'status' : 403 , 'errors' : serializer.errors , 'message' : 'something went wrong'})
    
    serializer.save()
    return Response({'status' : 200 , 'payload' : serializer.data , 'message' : 'you sent'})

@api_view(['PATCH'])
def update_Book(request,id):
    try: 
        Book_obj = Book.objects.get(pk = id)
    except :
        return Response({'status' : 403 , 'message' : 'invalid id'})     
    serializer = BookSerializer(Book_obj, data=request.data, partial =True)

    if serializer.is_valid():
        serializer.save()
        return Response({'data':serializer.data})     
    return Response({'status' : 403 , 'message' : serializer.error_messages,'error':serializer.errors})             
    #      if not serializer.is_valid():
    #          print(serializer.errors)
    #          return Response({'status' : 403 , 'errors' : serializer.errors , 'message' : 'something went wrong'})
    #      serializer.Save()
    #      return Response({'status' : 200 , 'payload' : serializer.data , 'message' : 'you sent'})
    #  except Exception as e:
    #      return Response({'status' : 403 , 'message' : 'invalid id'})
     

@api_view(['DELETE'])
def delete_Book(request,id):
    try:
        Book_obj = Book.objects.get(pk = id)
        Book_obj.delete()
        return Response({'status' : 200 , 'message' : 'deleted'})
    except :

        return Response({'status' : 403 , 'message' : 'invalid id'})
