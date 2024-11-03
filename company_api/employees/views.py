from django.shortcuts import render

# Create your views here.
from django_filters import rest_framework as filters
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


class EmployeeFilter(filters.FilterSet):
    department = filters.CharFilter(
        field_name='department', lookup_expr='exact')
    role = filters.CharFilter(field_name='role', lookup_expr='exact')

    class Meta:
        model = Employee
        fields = ['department', 'role']


class EmployeePagination(PageNumberPagination):
    page_size = 10


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = EmployeePagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EmployeeFilter

    def post(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
