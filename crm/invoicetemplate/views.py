from django.http import request
from rest_framework import parsers, serializers
from rest_framework.exceptions import APIException
from modules.ResponseHandler import ResponseHandler
from .models import InvoiceTemplate
from rest_framework import permissions, generics
from .serializer import InvoiceTemplateSerializer
from rest_framework.parsers import MultiPartParser
from modules.Paginator import BasePaginator
from django.db.models import Q

class ListCreateInvoiceTemplate(generics.ListCreateAPIView,ResponseHandler):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser]
    pagination_class = BasePaginator
    serializer_class = InvoiceTemplateSerializer

    def get_queryset(self):
        return InvoiceTemplate.objects.filter(Q(tenant__id=None)|Q(tenant__id=self.request.user.tenant.id))

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save(tenant=request.user.tenant)

            return self.response_created(serializer.data,'Template saved')
        except APIException as e:
                return self.response_unexpected(e)

class ShowUpdateDeleteInvoiceTemplate(generics.RetrieveUpdateDestroyAPIView,ResponseHandler):
  permission_classes = [permissions.IsAuthenticated]
  parser_classes = (parsers.MultiPartParser,)
  serializer_class = InvoiceTemplateSerializer
  queryset = ''

  def get(self,request, *args,**kwargs):
        queryset = InvoiceTemplate.objects.filter(tenant_id=self.request.user.tenant.id,uuid=self.kwargs['pk']).first()

        if not queryset:
            return self.response_notfound('Invoice template')

        try:
            serializer = self.get_serializer(queryset )
            return self.response_ok(serializer.data)
        except InvoiceTemplate.DoesNotExist:
            return self.response_notfound("InvoiceTemplate")

  def put(self,request, *args,**kwargs):
        queryset = InvoiceTemplate.objects.filter(tenant_id=self.request.user.tenant.id,uuid=self.kwargs['pk']).first()

        if not queryset:
            return self.response_notfound('Invoice template')

        try:
            serializer = self.get_serializer(queryset)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return self.response_ok(serializer.data,'InvoiceTemplate updated')
        except Exception as e:
            return self.response_unexpected(e)

  def delete(self,request, *args,**kwargs):
          queryset = InvoiceTemplate.objects.filter(tenant_id=self.request.user.tenant.id,uuid=self.kwargs['pk']).first()
          template = queryset

          if not queryset:
              return self.response_notfound('Invoice template')
          queryset.delete()
          return self.response_archived(f'Invoice template: {template.name}')
