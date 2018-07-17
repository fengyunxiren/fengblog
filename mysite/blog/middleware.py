# coding=utf-8
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class PostDenyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method != 'GET':
            return JsonResponse({'errcode': -1, 'errmsg': 'method is not allowed!'})