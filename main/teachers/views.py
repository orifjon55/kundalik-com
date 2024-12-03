from django.shortcuts import render
from main import models as md
from .import serializers as ser
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5

class TeachersView(ListAPIView):
    queryset = md.Teacher.objects.all()
    serializer_class = ser.TeachersSer
    pagination_class = CustomPagination

class TeacherSearch(ListAPIView):
    queryset = md.Teacher.objects.all()
    serializer_class = ser.TeachersSer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['fullname']
    filterset_fields = '__all__'