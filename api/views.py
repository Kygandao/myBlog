from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import Blog
from .serializers import BlogSerializer
from api import serializers
from .utils import createBlog, deleteBlog, getBlogsList, getBlogDetail

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/blogs/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of blogs'
        },
        {
            'Endpoint': '/blog/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single blog object'
        },
        {
            'Endpoint': '/blogs/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new blog with data sent in post request'
        },
        {
            'Endpoint': '/blogs/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting blog'
        },
    ]
    return Response(routes)

@api_view(['GET'])  
def getBlogs(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(['GET'])  
def getBlog(request, pk):
    blogs = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blogs, many=False)
    return Response(serializer.data)
