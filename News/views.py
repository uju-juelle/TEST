from django.shortcuts import render
from .models import News
from rest_framework.views import APIView
from .serializers import NewsSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class news_homepage(APIView):
    
    def get(self, request, format=None):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        current_user = request.user
        new_news = News(reporter=current_user)
        serializer = NewsSerializer(new_news, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


class news_detailpage(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, slug, format=None):
        detail = News.objects.get(slug=slug)
        serializer = NewsSerializer(detail)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, slug, format=None):
        detail = News.objects.get(slug=slug)
        current_user = request.user
        if current_user != detail.reporter:
            return Response("You cannot edit someone's news")
        else:
           serializer = NewsSerializer(detail, data=request.data, partial=True)
           serializer.is_valid(raise_exception=True)
           serializer.save()
           return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def delete(self, request, slug, format=None):
        detail = News.objects.get(slug=slug)
        current_user = request.user
        if current_user != detail.reporter:
            return Response("Stop it!!!!!")
        detail.delete()
        return Response("Successfully deleted", status=status.HTTP_204_NO_CONTENT)