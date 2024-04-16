from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Omonimlar
from .serializers import OmonimlarSerializer, ListOmonimlarSerializer


class OmonimlarViewSet(ModelViewSet):
    queryset = Omonimlar.objects.all()
    serializer_class = OmonimlarSerializer


class OmonimlarListView(APIView):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']

    def get(self, request):
        queryset = Omonimlar.objects.all()
        search_filter = SearchFilter()
        queryset = search_filter.filter_queryset(request, queryset, self)
        filter_backend = DjangoFilterBackend()
        queryset = filter_backend.filter_queryset(request, queryset, self)

        serializer = OmonimlarSerializer(queryset, many=True)
        return Response(serializer.data)
