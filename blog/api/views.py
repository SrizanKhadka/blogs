from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from blog.api.serializer import BlogSerializer
from blog.models import Blogs

class ListAllBlogsAPIView(ListCreateAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer
    