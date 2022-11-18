from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name="blog home"),
    path('blogpost/<int:id>', views.Blogpost,name="blogpost"),
]