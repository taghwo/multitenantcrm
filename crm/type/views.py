from contact.serializer import ContactReadOnlySerializer
from rest_framework.exceptions import APIException
from type.serializer import ClientTypeSerializer
from type.models import Type
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from modules.ResponseHandler import ResponseHandler
from modules.Paginator import BasePaginator

class ListCreateClientType(ListCreateAPIView,ResponseHandler):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ClientTypeSerializer
    pagination_class = BasePaginator

    def get_queryset(self):
        return Type.objects.filter(tenant__id=self.request.user.tenant.id).order_by('-created_at')

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,context={'tenant_id':request.user.tenant.id})
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save(tenant=request.user.tenant)
            getCleanData = ContactReadOnlySerializer(serializer)
            return self.response_created( getCleanData.data,'Type created')
        except APIException as e:
                return self.response_unexpected(e)


class ShowUpdateDeleteClientType(RetrieveUpdateDestroyAPIView,ResponseHandler):
      permission_classes = [permissions.IsAuthenticated]
      serializer_class = ClientTypeSerializer

      def get_queryset(self):
          return Type.objects.filter(pk=self.kwargs['pk']).filter(tenant__id=self.request.user.tenant.id).first()

      def get(self,request,pk):
          queryset = self.get_queryset()
          serializer = self.get_serializer(queryset)
          if not queryset:
              return self.response_notfound('Type')
          return self.response_ok(serializer.data)

      def put(self,request,pk):
          queryset = self.get_queryset()
          if not queryset:
              return self.response_notfound('Type')
          serializer = self.get_serializer(queryset,data=request.data,context={'tenant_id':request.user.tenant.id},partial=True)
          serializer.is_valid(raise_exception=True)
          serializer.save()
          return self.response_ok(serializer.data,'Type updated')

      def delete(self,request,pk):
          queryset = self.get_queryset()
          type = self.get_queryset()
          if not queryset:
              return self.response_notfound('Type')
          queryset.delete()
          return self.response_archived(f'Type: {type.name}')
