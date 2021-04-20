from rest_framework.exceptions import APIException
from invoice.serializer import InvoiceReadSerializer, InvoiceWriteSerializer
from invoice.models import Invoice
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from modules.ResponseHandler import ResponseHandler
from modules.Paginator import BasePaginator

class ListCreateInvoice(ListCreateAPIView,ResponseHandler):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = InvoiceReadSerializer
    pagination_class = BasePaginator

    def get_queryset(self):
        return Invoice.objects.filter(tenant__id=self.request.user.tenant.id).order_by('-created_at')

    def post(self, request, *args, **kwargs):
        serializer = InvoiceWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save(tenant=request.user.tenant,created_by=request.user)

            data = Invoice.objects.get(pk=serializer.data['id'])

            new_invoice = InvoiceReadSerializer(data)
            return self.response_created(new_invoice.data,'Invoice created')
        except APIException as e:
                return self.response_unexpected(e)


class ShowUpdateDeleteInvoice(RetrieveUpdateDestroyAPIView,ResponseHandler):
      permission_classes = [permissions.IsAuthenticated]
      serializer_class = InvoiceReadSerializer

      def get_queryset(self):
          return Invoice.objects.filter(uuid=self.kwargs['pk'],tenant__id=self.request.user.tenant.id).first()

      def get(self,request,pk):
          queryset = self.get_queryset()
          serializer = self.get_serializer(queryset)
          if not queryset:
              return self.response_notfound('Invoice')
          return self.response_ok(serializer.data)

      def put(self,request,pk):
          queryset = self.get_queryset()
          if not queryset:
              return self.response_notfound('Invoice')
          serializer = InvoiceWriteSerializer(queryset,data=request.data,context={'tenant_id':request.user.tenant.id},partial=True)
          serializer.is_valid(raise_exception=True)
          serializer.save(updated_by=request.user)
          return self.response_ok(serializer.data,'Invoice updated')

      def delete(self,request,pk):
          queryset = self.get_queryset()
          invoice = self.get_queryset()
          if not queryset:
              return self.response_notfound('Invoice')
          queryset.delete()
          return self.response_archived(f'Invoice: {invoice.name}')
