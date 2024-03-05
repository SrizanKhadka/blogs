from rest_framework import serializers
from blog.models import Blogs, Category, Comments


class CommentSerializer(serializers.ModelSerializer):
    
    blog_title = serializers.CharField(source="blog.blog_title")
    commenter = serializers.CharField(source="commenter.username")

    class Meta:
        model = Comments
        fields = ["comment", "blog_title", "commenter"]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    
    blog_comments = CommentSerializer(many=True, read_only=True)
    blog_category = serializers.StringRelatedField()

    class Meta:
        model = Blogs
        fields = "__all__"
