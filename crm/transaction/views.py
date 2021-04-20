from rest_framework.exceptions import APIException
from transaction.serializer import TransactionReadSerializer, TransactionWriteSerializer
from transaction.models import Transaction
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from modules.ResponseHandler import ResponseHandler
from modules.Paginator import BasePaginator

class ListCreateTransaction(ListCreateAPIView,ResponseHandler):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TransactionReadSerializer
    pagination_class = BasePaginator

    def get_queryset(self):
        return Transaction.objects.filter(tenant__id=self.request.user.tenant.id).order_by('-created_at')

    def post(self, request, *args, **kwargs):
        serializer = TransactionWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save(tenant=request.user.tenant,created_by=request.user)

            data = Transaction.objects.get(pk=serializer.data['id'])

            new_transaction = TransactionReadSerializer(data)
            return self.response_created(new_transaction.data,'Transaction created')
        except APIException as e:
                return self.response_unexpected(e)


class ShowUpdateDeleteTransaction(RetrieveUpdateDestroyAPIView,ResponseHandler):
      permission_classes = [permissions.IsAuthenticated]
      serializer_class = TransactionReadSerializer

      def get_queryset(self):
          return Transaction.objects.filter(uuid=self.kwargs['pk'],tenant__id=self.request.user.tenant.id).first()

      def get(self,request,pk):
          queryset = self.get_queryset()
          serializer = self.get_serializer(queryset)
          if not queryset:
              return self.response_notfound('Transaction')
          return self.response_ok(serializer.data)

      def put(self,request,pk):
          queryset = self.get_queryset()
          if not queryset:
              return self.response_notfound('Transaction')
          serializer = TransactionWriteSerializer(queryset,data=request.data,context={'tenant_id':request.user.tenant.id},partial=True)
          serializer.is_valid(raise_exception=True)
          serializer.save(updated_by=request.user)
          return self.response_ok(serializer.data,'Transaction updated')

      def delete(self,request,pk):
          queryset = self.get_queryset()
          transaction = self.get_queryset()
          if not queryset:
              return self.response_notfound('Transaction')
          queryset.delete()
          return self.response_archived(f'Transaction: {transaction.name}')
