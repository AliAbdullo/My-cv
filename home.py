from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .permissions import IsAdminOrCreateOnly
from .filters import DateRangeFilterBackend
from . import serializers
from .models import *

class HomiyView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrCreateOnly]
    queryset = Homiy.objects.all()
    serializer_class = serializers.HomiySerializer
    filter_backends = [DateRangeFilterBackend, SearchFilter, DjangoFilterBackend]
    search_fields = ['full_name', 'company_name']
    filterset_fields = ['money', 'status']
    date_range_filter_fields = ['date_created']


class HomiyDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Homiy.objects.all()
    serializer_class = serializers.HomiySerializer

class TalabaView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Talaba.objects.all()
    serializer_class = serializers.TalabaSerializer
    filter_backends = [DateRangeFilterBackend, SearchFilter, DjangoFilterBackend]
    search_fields = ['full_name']
    filterset_fields = ['degree', 'universitet']
    date_range_filter_fields = ['date_created']
