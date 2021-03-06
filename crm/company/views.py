from django.shortcuts import render

from rest_framework.exceptions import APIException
from company.serializer import CompanySerializer
from company.models import Company
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from modules.ResponseHandler import ResponseHandler
from modules.Paginator import BasePaginator

class ListCreateCompany(ListCreateAPIView,ResponseHandler):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CompanySerializer
    pagination_class = BasePaginator

    def get_queryset(self):
        return Company.objects.filter(tenant__id=self.request.user.tenant.id).order_by('-created_at')

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,context={'tenant_id':request.user.tenant.id})
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save(tenant=request.user.tenant,created_by=request.user)
            return self.response_created(serializer.data,'Company created')
        except APIException as e:
                return self.response_unexpected(e)


class ShowUpdateDeleteCompany(RetrieveUpdateDestroyAPIView,ResponseHandler):
      permission_classes = [permissions.IsAuthenticated]
      serializer_class = CompanySerializer

      def get_queryset(self):
          return Company.objects.filter(pk=self.kwargs['pk']).filter(tenant__id=self.request.user.tenant.id).first()

      def get(self,request,pk):
          queryset = self.get_queryset()
          serializer = self.get_serializer(queryset)
          if not queryset:
              return self.response_notfound('Company')
          return self.response_ok(serializer.data)

      def put(self,request,pk):
          queryset = self.get_queryset()
          if not queryset:
              return self.response_notfound('Company')
          serializer = self.get_serializer(queryset,data=request.data,context={'tenant_id':request.user.tenant.id,'pk':self.kwargs['pk']},partial=True)
          serializer.is_valid(raise_exception=True)
          serializer.save(updated_by=request.user)
          return self.response_ok(serializer.data,'company updated')

      def delete(self,request,pk):
          queryset = self.get_queryset()
          company = self.get_queryset()
          if not queryset:
              return self.response_notfound('company')
          queryset.delete()
          return self.response_archived(f'company: {company.name}')

