from rest_framework import serializers
from .models import Omonimlar


class OmonimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Omonimlar
        fields = '__all__'


class ListOmonimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Omonimlar
        fields = ['id', 'name']


class CreateOmonimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Omonimlar
        fields = ['name', 'description', 'author']


class UpdateOmonimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Omonimlar
        fields = ['name', 'description', 'author']


class DeleteOmonimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Omonimlar
        fields = ['id', ]

