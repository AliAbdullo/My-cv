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


class TalabaDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Talaba.objects.all()
    serializer_class = serializers.TalabaSerializer


class HomiyshipView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Homiyship.objects.all()
    serializer_class = serializers.HomiyshipSerializer
    filter_backends = [DateRangeFilterBackend, SearchFilter, DjangoFilterBackend]
    search_fields = ['Homiy__full_name', 'Homiy__company_name', 'Talaba__full_name']
    date_range_filter_fields = ['date_created']


class HomiyshipDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Homiyship.objects.all()
    serializer_class = serializers.HomiyshipSerializer


class HomiyshipsByTalabaView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = serializers.HomiyshipsByTalabaSerializer

    def get_queryset(self):
        Talaba = get_object_or_404(Talaba, id=self.kwargs['pk'])
        queryset = Talaba.Homiyships.all()
        return queryset


class HomiyshipsByHomiyView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = serializers.HomiyshipsByHomiySerializer

    def get_queryset(self):
        Homiy = get_object_or_404(Homiy, id=self.kwargs['pk'])
        queryset = Homiy.Homiyships.all()
        return queryset


class UniversitetView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Universitet.objects.all()
    serializer_class = serializers.UniversitetSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']


class UniversitetDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Universitet.objects.all()
    serializer_class = serializers.UniversitetSerializer


class DashboardView(APIView):
    permission_classes = [IsAdminUser]

    @staticmethod
    def get(request, *args, **kwargs):
        dashboard_money_serializer = serializers.DashboardMoneySerializer()
        dashboard_graph_serializer = serializers.DashboardGraphSerializer()
        return Response(data={
            'money_stats': dashboard_money_serializer.data,
            'graph_stats': dashboard_graph_serializer.data
        })
        
        
        
        
        
        
        
        











def validate_positive(value):
    if value > 0:
        return value
    else:
        raise ValidationError('Positive integer is required')


def validate_homiyship_money_on_update(instance, validated_data):
    HomiyshipsByHomiyView = get_object_or_404(Homiy, id=validated_data['homiy_id'])
    talaba = instance.talaba
    money = validated_data['money']

    homiy_spent_money = \
        homiy.homiyships.exclude(id=instance.id).aggregate(money_sum=Coalesce(Sum('money'), 0))['money_sum']
    talaba_gained_money = \
        talaba.homiyships.exclude(id=instance.id).aggregate(money_sum=Coalesce(Sum('money'), 0))['money_sum']
    homiy_left_money = homiy.money - homiy_spent_money

    if money <= homiy_left_money:
        if talaba_gained_money + money <= talaba.contract:
            instance.money = money
            instance.homiy = homiy
            instance.save()
            return instance
        else:
            raise ValidationError({'money': 'Homiylik puli kontrakt miqdoridan oshib ketdi'})
    else:
        raise ValidationError({'money': 'Homiyda buncha pul mavjud emas.'})


def validate_homiyship_money_on_create(validated_data):
    homiy = get_object_or_404(Homiy, id=validated_data.get('homiy_id'))
    talaba = get_object_or_404(Talaba, id=validated_data.get('talaba_id'))
    money = validated_data.get('money')

    homiy_spent_money = homiy.homiyships.aggregate(money_sum=Coalesce(Sum('money'), 0))['money_sum']
    talaba_gained_money = talaba.homiyships.aggregate(money_sum=Coalesce(Sum('money'), 0))['money_sum']
    homiy_left_money = homiy.money - homiy_spent_money

    if money <= homiy_left_money:
        if talaba_gained_money + money <= talaba.contract:
            homiyship = homiyship.objects.create(**validated_data)
            return homiyship
        else:
            raise ValidationError({'money': 'Homiylik puli kontrakt miqdoridan ochib ketdi'})
    else:
        raise ValidationError({'money': 'Homiyda buncha pul mavjud emas.'})        
        