from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer

def createBlog(request):
    data = request.data
    note = Blog.objects.create(
        body=data['body']
    )
    serializer = BlogSerializer(note, many=False)
    return Response(serializer.data)

def deleteBlog(request, pk):
    note = Blog.objects.get(id=pk)
    note.delete()
    return Response('Deleted.')

def getBlogsList(request):
    blogs = Blog.objects.all().order_by('-updated')
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


def getBlogDetail(request, pk):
    blogs = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blogs, many=False)
    return Response(serializer.data)