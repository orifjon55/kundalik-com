from django.shortcuts import render
from . import serializers as ser
from main import models as md
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5

class PrincipalView(ListAPIView):
    queryset = md.Principal.objects.all()
    serializer_class = ser.PrincipalSer
    pagination_class = CustomPagination

class SearchView(ListAPIView):
    queryset = md.Principal.objects.all()
    serializer_class = ser.PrincipalSer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['fullname']
    filterset_fields = '__all__'