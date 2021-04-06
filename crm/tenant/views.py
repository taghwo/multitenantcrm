from rest_framework import parsers, serializers
from modules.ResponseHandler import ResponseHandler
from .models import Tenant
from rest_framework import permissions, generics
from .serializer import TenantSerializer, TenantAccountsSerializer
from rest_framework.parsers import MultiPartParser
from modules.Paginator import BasePaginator


class ListCreateTenant(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser]
    pagination_class = BasePaginator

    def get_queryset(self):
        return Tenant.objects.all()

    def get_serializer(self, *args, **kwargs):
        param = self.request.query_params.get('withAccounts', None)
        if param is not None:
            return TenantAccountsSerializer(self.get_queryset(), many=True)
        else:
            return TenantSerializer(self.get_queryset(), many=True)

class ShowUpdateDeleteTenant(generics.RetrieveUpdateDestroyAPIView,ResponseHandler):
  permission_classes = [permissions.IsAuthenticated]
  parser_classes = (parsers.MultiPartParser,)
  serializer_class = TenantSerializer

  def get_queryset(self):
      return Tenant.objects.get(pk=self.request.user.tenant.id)

  def get(self,request, *args,**kwargs):

      try:
          serializer = self.get_serializer(self.get_queryset())
          return self.response_ok(serializer.data)
      except Tenant.DoesNotExist:
          return self.response_notfound("Tenant")

  def put(self,request, *args,**kwargs):
      try:
          serializer = self.get_serializer(self.get_queryset(), data=request.data)
          serializer.is_valid(raise_exception=True)
          serializer.save()
          return self.response_ok(serializer.data,'Business info updated')
      except Exception as e:
          return self.response_error(e.args)

#   def delete(self,request, *args,**kwargs):
#       try:
#           tenant = self.get_queryset()
#           tenant.delete()
#           return self.response_archived("Tenant deleted")
#       except Tenant.DoesNotExist:
#           return self.response_notfound("Tenant")