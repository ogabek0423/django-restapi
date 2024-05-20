from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from users.models import Problems, Comments, Agents
from .serializers import CategorySerializer
from .serializers import ApartmentSerializer, AgentsSerializer, AddressSerializer, SellTypeSerializer
from .serializers import ProblemsSerializer, UserSerializer, CitySerializer, CommentsSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from django.db.transaction import atomic
from projectapp.models import Category, Apartment, Address, SellType, City


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', '^name']
    pagination_class = LimitOffsetPagination


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'name']
    pagination_class = LimitOffsetPagination


class SellTypeViewSet(ModelViewSet):
    queryset = SellType.objects.all()
    serializer_class = SellTypeSerializer
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'name']
    pagination_class = LimitOffsetPagination


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'city', 'name']
    pagination_class = LimitOffsetPagination


class ApartmentViewSet(ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['category', 'address', 'sell_type', 'short_name',
                     'description', 'phone', 'square', 'seller_name', 'seller_phone',
                     'count_floor', 'count_bedrooms', 'views']
    pagination_class = LimitOffsetPagination


class CommentViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'user', 'comment', 'comment_title']
    pagination_class = LimitOffsetPagination


class ProblemViewSet(ModelViewSet):
    queryset = Problems.objects.all()
    serializer_class = ProblemsSerializer
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'firstname', 'email', 'problem_name', 'problem_description']
    pagination_class = LimitOffsetPagination


class ApartmentsViewSet(ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['category', 'sell_type', 'short_name', 'square', 'rooms',
                     'price', 'description', 'seller_phone', 'seller_name']
    pagination_class = LimitOffsetPagination