from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Banks, Branches
from django.views import View
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import BankSerializer, BranchesSerializer
from django.shortcuts import render
from rest_framework.pagination import LimitOffsetPagination
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated 

class BankView(viewsets.ModelViewSet):
         
        queryset = Banks.objects.all()
        serializer_class = BankSerializer

class BranchesView(viewsets.ModelViewSet):
        permission_classes = (IsAuthenticated,)
        queryset = Branches.objects.all()
        serializer_class = BranchesSerializer
        
class DetailView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,) 
    def get(self, request, ifsc):
        branch = Branches.objects.filter(ifsc__iexact=ifsc).first()
        serializer = BranchesSerializer(branch)
        return Response(serializer.data)


class ListView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,) 
    pagination_class = LimitOffsetPagination
    def get(self, request, city, bank):
        branch_qset = Branches.objects.filter(
            city__iexact=city, bank__name__icontains=bank)
        serializer = BranchesSerializer(branch_qset, many=True)
        serializer = self.get_pagination_serializer(serializer)
        return Response(serializer.data)
