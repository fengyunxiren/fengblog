from rest_framework import routers
from blog.views import CategoryViewSet
from blog.views import AuthorViewSet
from blog.views import ArticleViewSet
from blog.views import ImageViewSet
from django.urls import path, include
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'article', ArticleViewSet)
router.register(r'image', ImageViewSet)

urlpatterns = [
    url('', include(router.urls)),
]