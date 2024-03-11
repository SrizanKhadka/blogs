from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from blog.api.serializer import BlogSerializer
from blog.models import Blogs
from rest_framework import permissions

class ListAllBlogsAPIView(ListCreateAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CreateBlogsAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]



    
