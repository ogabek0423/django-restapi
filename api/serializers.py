from rest_framework import serializers
from projectapp.models import Address, Apartment, City, Category, SellType
from users.models import Comments, Problems, Agents
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'country']


class AddressSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    class Meta:
        model = Address
        fields = ['id', 'city', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'views', 'image']


class SellTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellType
        fields = ['id', 'name']


class AgentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agents
        fields = ['id', 'firstname', 'lastname', 'email', 'username', 'password', 'phone', 'work_price', 'work_time',
                  'experience', 'count_sold', 'views', 'photo']


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'user', 'comment_title', 'comment']


class ProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problems
        fields = ['id', 'firstname', 'email', 'problem_name', 'problem_description']


class ApartmentSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    sell_type = SellTypeSerializer(read_only=True)
    agents = AgentsSerializer(read_only=True)
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Apartment
        fields = ['seller_name', 'seller_phone', 'phone', 'work_price', 'work_time', 'experience',
                  'count_sold', 'photo1', 'photo2', 'views', 'price']

