# coding=utf-8

from rest_framework import serializers
from blog.models import Category
from blog.models import Author
from blog.models import Article
from blog.models import Images


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'update_time', 'name', 'describle']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'update_time', 'name', 'nickname', 'gender', 'signature']


class ArticleSerializer(serializers.ModelSerializer):
    nickname = serializers.ReadOnlyField(source='author.nickname')
    category_name = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Article
        fields = ['id', 'update_time', 'title', 'describle', 'author',
                  'category', 'content', 'nickname', 'category_name']


class ImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=256, use_url=False)
    class Meta:
        model = Images
        fields = ['id', 'update_time', 'name', 'image']