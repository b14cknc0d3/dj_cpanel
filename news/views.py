from functools import partial
from math import exp
from django.db.models.query import QuerySet
from django.http.request import QueryDict
from django.utils import translation
from rest_framework.views import APIView
from news.models import Comment, DeviceID, Like, News
from django.db import models
from news.serializers import CommentSerializer, DeviceIDSerializer, LikeSerializer, NewsSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import  status
import json
# Create your views here.

class NewsApiView(ListAPIView):
    model = News
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    permission_classes =  [IsAuthenticatedOrReadOnly,]
    
    # def filter_queryset(self, queryset):
    #     qs = self.queryset
    #     fqs = qs.filter()
    

class LikeCreateView(CreateAPIView):
    model = Like
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    permission_classes =  [AllowAny]
    
    def post(self, request, *args, **kwargs):
        ip_address = request.META.get('REMOTE_ADDR', '')[:63] or None
        
        user_agent =self.request.META.get('HTTP_USER_AGENT', '')[:255] or None
        s = DeviceIDSerializer(data={"ip_address":ip_address,"user_agent":user_agent})
        like_data  =  self.request.data["like"] 
        print(like_data)
        device = DeviceID.objects.filter(ip_address=ip_address)
        if not device.exists():
            if s.is_valid():
                s.save()
        
        try:
            news_id : QuerySet = News.objects.filter(pk=self.kwargs["pk"])
            print(news_id);
            if news_id.exists() :
                
                deviceId : DeviceID =device.first()
                newsID : News = news_id.first()
                like = Like.objects.filter(device_id=deviceId,news_id=newsID)
                if like.exists():
                    
                    # like_status: Like = like.first()
                    # like_update: bool =like_status.like
                    # change_like: bool = not like_update
                    # like_status.like = like_data
                    # like_status.save()
                    data = {"like":like_data}
                    
                    result = LikeSerializer(instance=like.first(),data=data,partial=True)
                    if result.is_valid():
                        result.update(instance=like.first(),validated_data=data)
                        result.save()
                        return Response(data=result.data,status=status.HTTP_201_CREATED)
                    else:
                        return Response(data={"error":str(result.errors)},status=status.HTTP_400_BAD_REQUEST)
                    # if ls.is_valid():
                    #     try:
                    #         ls.update()
                    #         print("like created")
                    #         return Response(data=ls.data,status=status.HTTP_201_CREATED)
                    #     except Exception as e:
                    #         return Response(data={"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
                    # else:
                    #     return Response(data={"error":"serializer is not valid!"},status=status.HTTP_400_BAD_REQUEST)
                        

                else:
                    data = {"like":like_data or True,"device_id":deviceId.pk,"news_id":newsID.pk}
                    ls = LikeSerializer(data=data)
                    if ls.is_valid():
                        try:
                            ls.save()
                            print("like created")
                            return Response(data=ls.data,status=status.HTTP_201_CREATED)
                        except Exception as e:
                            return Response(data={"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response(data={"error":"serializer is not valid!"},status=status.HTTP_400_BAD_REQUEST)
                    
            else:
                 return Response(data={"error":"no news related to"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as  e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class CommentlistCreateView(ListCreateAPIView):
    model =Comment
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
    queryset =Comment.objects.all()
    
    def filter_queryset(self, queryset):
        qs  = self.queryset
        qs  = qs.filter(news_id=self.kwargs['pk'])
        return qs
    
    
    
    def post(self, request, *args, **kwargs):
        
        ip_address = request.META.get('REMOTE_ADDR', '')[:63] or None
        
        user_agent =self.request.META.get('HTTP_USER_AGENT', '')[:255] or None
        s = DeviceIDSerializer(data={"ip_address":ip_address,"user_agent":user_agent})
      
        comment = self.request.POST.get("comment","") or self.request.data["comment"] or None
        
        if comment is not None:
            # print(comment)
            # comment = comment.replace("\n","\\n")
            # comment = comment.replace("\r","\\r")
            print(comment)
            
            
            
        device = DeviceID.objects.filter(ip_address=ip_address)
        if not device.exists():
            if s.is_valid():
                s.save()
       
        try:
            
            news_id : QuerySet = News.objects.filter(pk=self.kwargs["pk"])
            if news_id.exists():
                deviceId : DeviceID =device.first()
                newsID : News = news_id.first()
                data = {"news_id":newsID.pk,"device_id":deviceId.pk,"comment":comment}
                
                serializers = CommentSerializer(data=data)
                if serializers.is_valid():
                    serializers.save()
                    return Response(serializers.data,status=status.HTTP_201_CREATED)
                else:
                    # raise Exception(serializers.errors)
                    return Response({"error":str(serializers.errors) + "data =>" + str(data) },status=status.HTTP_400_BAD_REQUEST)                
                
            else:
                return Response({"error":"post doesn't exist!"},status=status.HTTP_400_BAD_REQUEST)
            
            
        except Exception as e:
            # raise Exception(e)
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
            

        
        

