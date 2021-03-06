from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import detail_route, list_route
from blog.serializers import CategorySerializer
from blog.models import Category
from blog.serializers import AuthorSerializer
from blog.models import Author
from blog.serializers import ArticleSerializer
from blog.models import Article
from blog.serializers import ImagesSerializer
from blog.models import Images
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(is_delete=False)
    serializer_class = CategorySerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.filter(is_delete=False)
    serializer_class = AuthorSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(is_delete=False)
    serializer_class = ArticleSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.filter(is_delete=False)
    serializer_class = ImagesSerializer
