from blog.api.views import *
from django.urls import path

urlpatterns = [
    path("blogs-list/", ListAllBlogsAPIView.as_view(), name="blogs/list"),
    path("create/blogs/<int:pk>", CreateBlogsAPIView.as_view(), name="blogs/create")
]
