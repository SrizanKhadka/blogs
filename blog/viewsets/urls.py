from blog.viewsets import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.contrib import admin


router = DefaultRouter()
router.register("users", views.UserViewSets, basename="user")
urlpatterns = [
    path("users", include(router.urls))
    ]