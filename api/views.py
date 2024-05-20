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
from django.utils import timezone
from datetime import datetime


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', '^name']
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET'])
    def open_page(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = CategorySerializer(category, many=False)
        created = category.create_time
        return Response(data={'created': created}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def last_updated(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = CategorySerializer(category, many=False)
        updated = category.update_time
        return Response(data={'updated': updated}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def views(self, request, *args, **kwargs):
        category = self.get_object()
        with atomic():
            category.views = category.views + 1
            category.save()
            return Response(status.HTTP_204_NO_CONTENT)


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'name']
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET'])
    def last_updated(self, request, *args, **kwargs):
        city = self.get_object()
        serializer = CitySerializer(city, many=False)
        updated = city.last_update_time
        return Response(data={'updated': updated}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def abs_list(self, request, *args, **kwargs):
        city = self.get_queryset()
        city = city.order_by('name')
        serializer = CitySerializer(city, many=True)
        return Response(data=serializer.data)


class SellTypeViewSet(ModelViewSet):
    queryset = SellType.objects.all()
    serializer_class = SellTypeSerializer
    # permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'name']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['GET'])
    def last_updated(self, request, *args, **kwargs):
        with atomic():
            today = datetime.now().date()
            results = []
            for sell in self.get_queryset():
                day = (today - sell.create_time.date()).days
                results.append({
                    'id': sell.id,
                    'update_time': sell.create_time,
                    'days_since_update': day,
                })
            return Response(data=results, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def abs_list(self, request, *args, **kwargs):
        sell = self.get_queryset()
        sell = sell.order_by('name')
        serializer = SellTypeSerializer(sell, many=True)
        return Response(data=serializer.data)


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    # permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'city', 'name']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['GET'])
    def last_updated(self, request, *args, **kwargs):
        with atomic():
            today = datetime.now().date()
            results = []
            for sell in self.get_queryset():
                day = (today - sell.last_update_time.date()).days
                results.append({
                    'id': sell.id,
                    'update_time': sell.last_update_time,
                    'days_since_update': day,
                })
            return Response(data=results, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def abs_list(self, request, *args, **kwargs):
        address = self.get_queryset()
        address = address.order_by('name')
        serializer = AddressSerializer(address, many=True)
        return Response(data=serializer.data)


class ApartmentViewSet(ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['category', 'address', 'sell_type', 'short_name',
                     'description', 'phone', 'square', 'seller_name', 'seller_phone',
                     'count_floor', 'count_bedrooms', 'views']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['GET'])
    def abs_list(self, request, *args, **kwargs):
        apartment = self.get_queryset()
        apartment = apartment.order_by('short_name')
        serializer = ApartmentSerializer(apartment, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET'])
    def last_updated(self, request, *args, **kwargs):
        with atomic():
            today = datetime.now().date()
            results = []
            for sell in self.get_queryset():
                day = (today - sell.reconstruct_date.date()).days
                results.append({
                    'id': sell.id,
                    'update_time': sell.reconstruct_date,
                    'days_since_update': day,
                })
            return Response(data=results, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def views(self, request, *args, **kwargs):
        apartment = self.get_object()
        with atomic():
            apartment.views = apartment.views + 1
            apartment.save()
            return Response(status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['GET'])
    def open_page(self, request, *args, **kwargs):
        apartment = self.get_object()
        serializer = ApartmentSerializer(apartment, many=False)
        created = apartment.build_date
        return Response(data={'created': created}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        apartment = self.get_queryset()
        apartment = apartment.order_by('price')
        serializer = ApartmentSerializer(apartment, many=True)
        return Response(data=serializer.data)


class CommentViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    # permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'user', 'comment', 'comment_title']
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET'])
    def open_comment(self, request, *args, **kwargs):
        comment = self.get_object()
        serializer = CommentsSerializer(comment, many=False)
        created = comment.created
        return Response(data={'created': created}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        comment = self.get_queryset()
        comment = comment.order_by('comment_title')
        serializer = ApartmentSerializer(comment, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET'])
    def last_updated(self, request, *args, **kwargs):
        with atomic():
            today = datetime.now().date()
            results = []
            for sell in self.get_queryset():
                day = (today - sell.created.date()).days
                results.append({
                    'id': sell.id,
                    'update_time': sell.created,
                    'days_since_update': day,
                })
            return Response(data=results, status=status.HTTP_200_OK)


class ProblemViewSet(ModelViewSet):
    queryset = Problems.objects.all()
    serializer_class = ProblemsSerializer
    # permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'firstname', 'email', 'problem_name', 'problem_description']
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET'])
    def write_problem_time(self, request, *args, **kwargs):
        problem = self.get_object()
        serializer = ProblemsSerializer(problem, many=False)
        created = problem.created_at
        return Response(data={'created': created}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        problem = self.get_queryset()
        problem = problem.order_by('created_at')
        serializer = ProblemsSerializer(problem, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['GET'])
    def last_updated(self, request, *args, **kwargs):
        with atomic():
            today = datetime.now().date()
            results = []
            for sell in self.get_queryset():
                day = (today - sell.created_at.date()).days
                results.append({
                    'id': sell.id,
                    'update_time': sell.created_at,
                    'days_since_update': day,
                })
            return Response(data=results, status=status.HTTP_200_OK)


class AgentsViewSet(ModelViewSet):
    queryset = Agents.objects.all()
    serializer_class = AgentsSerializer
    # permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['firstname', 'lastname', 'email', 'username', 'phone',
                     'work_price', 'views', 'experience']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['GET'])
    def sum(self, request, *args, **kwargs):
        for obj in self.queryset:
            s = obj.work_price * obj.count_sold
        context ={
            'work_price': obj.work_price,
            'sum': s
        }
        return Response(data=context, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        agent = self.get_queryset()
        agent = agent.order_by('work_price')
        serializer = AgentsSerializer(agent, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['GET'])
    def views(self, request, *args, **kwargs):
        agent = self.get_object()
        with atomic():
            agent.views = agent.views + 1
            agent.save()
            return Response(status.HTTP_204_NO_CONTENT)

