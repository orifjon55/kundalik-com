from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from .import serializers as ser
from main import models as md

class CustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5


class WorkView(APIView):
    def get(request,self,format = None):
        model = md.Assignment.objects.all()
        serializer = ser.WorkSer(model,many = True)
        pagination_class = CustomPagination
        return Response(serializer.data)
    
    
class WorkStatus(APIView):
    def get(request,self,format = None):
        model = md.AssignmentStatus.objects.all()
        serializer = ser.WorkStatusSer(model,many = True)
        return Response(serializer.data)
    
class WorkSearch(ListAPIView):
    queryset = md.Assignment.objects.all().order_by('id')
    serializer_class = ser.WorkSer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['fullname']
    filterset_fields = '__all__'