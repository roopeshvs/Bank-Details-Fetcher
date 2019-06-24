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
from django.conf import settings

class BankView(viewsets.ModelViewSet):
         
        queryset = Banks.objects.all()
        serializer_class = BankSerializer

class BranchesView(viewsets.ModelViewSet):
        permission_classes = (IsAuthenticated,)
        queryset = Branches.objects.all()
        serializer_class = BranchesSerializer
        
class DetailView(APIView):
    permission_classes = (IsAuthenticated,) 
    def get(self, request, ifsc):
        branch = Branches.objects.filter(ifsc__iexact=ifsc).first()
        serializer = BranchesSerializer(branch)
        return Response(serializer.data)


class ListView(APIView):
    permission_classes = (IsAuthenticated,) 
    pagination_class = LimitOffsetPagination
    def get(self, request, city, bank):
        branch_qset = Branches.objects.filter(
            city__iexact=city, bank__name__icontains=bank)
        page = self.paginate_queryset(self.branch_qset)
        serializer = BranchesSerializer(branch_qset, many=True)
        return self.get_paginated_response(serializer.data)

    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
         """
        Return a single page of results, or `None` if pagination is disabled.
        """
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
         """
        Return a paginated style `Response` object for the given output data.
        """
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)
