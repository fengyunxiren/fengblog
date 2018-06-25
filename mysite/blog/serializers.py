# coding=utf-8

from rest_framework import serializers
from blog.models import Category
from blog.models import Author
from blog.models import Article


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'update_time', 'name', 'describle']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'update_time', 'name', 'nickname', 'gender', 'signature']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'update_time', 'title', 'describle', 'author',
                  'category', 'content']