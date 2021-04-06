from modules.ResponseHandler import ResponseHandler
from contact.models import Contact
from modules.Paginator import BasePaginator
from contact.serializer import ContactReadOnlySerializer,ContactWriteSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions,parsers

class ListCreateContact(ListCreateAPIView,ResponseHandler):
    permission_classes = [permissions.IsAuthenticated]
    permission_parser = [parsers.MultiPartParser]
    serializer_class = ContactReadOnlySerializer
    pagination_class = BasePaginator

    def get_queryset(self):
        return Contact.objects.filter(tenant__id=self.request.user.tenant.id).order_by('-created_at')


    def post(self,request,*args,**kwargs):

        serializer = ContactWriteSerializer(data=request.data,context={'request':request,'tenant_id':request.user.tenant.id})

        serializer.is_valid(raise_exception=True)

        try:
             serializer.save(tenant=request.user.tenant,created_by=request.user)

             data = Contact.objects.get(pk=serializer.data['id'])

             new_contact = ContactReadOnlySerializer(data)

             return self.response_created(new_contact.data,"Contact created")
        except Exception as e:
            return self.response_unexpected(e)


class ShowUpdateDelete(RetrieveUpdateDestroyAPIView,ResponseHandler):
    permission_classes = [permissions.IsAuthenticated]
    permission_parser = [parsers.MultiPartParser]
    serializer_class = ContactReadOnlySerializer

    def get_queryset(self):
        return Contact.objects.filter(pk=self.kwargs['pk']).filter(tenant__id=self.request.user.tenant.id).first()


    def get(self,request,*args,**kwargs):
          queryset = self.get_queryset()
          serializer = self.get_serializer(queryset)
          if not queryset:
              return self.response_notfound('Contact')
          return self.response_ok(serializer.data)

    def put(self,request,*args,**kwargs):
        queryset = self.get_queryset()

        serializer = ContactWriteSerializer(queryset,data=request.data,context={'request':request,'tenant_id':request.user.tenant.id},partial=True)

        serializer.is_valid(raise_exception=True)

        try:
            serializer.save(tenant=request.user.tenant, updated_by=request.user)
            return self.response_ok(serializer.data,'Contact updated')
        except Exception as e:
            return self.response_unexpected(e.args)

    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        contact = self.get_queryset()

        if queryset is not None:
            queryset.delete()
            return self.response_archived(f"contact: {contact.first_name}")
        return self.response_notfound("Contact")
