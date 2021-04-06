from rest_framework.exceptions import APIException
from task.serializer import TaskReadSerializer, TaskWriteSerializer
from task.models import Task
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from modules.ResponseHandler import ResponseHandler
from modules.Paginator import BasePaginator

class ListCreateTask(ListCreateAPIView,ResponseHandler):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskReadSerializer
    pagination_class = BasePaginator

    def get_queryset(self):
        return Task.objects.filter(tenant__id=self.request.user.tenant.id).order_by('-created_at')

    def post(self, request, *args, **kwargs):
        serializer = TaskWriteSerializer(data=request.data,context={'tenant_id':request.user.tenant.id})
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save(tenant=request.user.tenant,created_by=request.user)

            data = Task.objects.get(pk=serializer.data['id'])

            new_task = TaskReadSerializer(data)
            return self.response_created(new_task.data,'Task created')
        except APIException as e:
                return self.response_unexpected(e)


class ShowUpdateDeleteTask(RetrieveUpdateDestroyAPIView,ResponseHandler):
      permission_classes = [permissions.IsAuthenticated]
      serializer_class = TaskReadSerializer

      def get_queryset(self):
          return Task.objects.filter(pk=self.kwargs['pk']).filter(tenant__id=self.request.user.tenant.id).first()

      def get(self,request,pk):
          queryset = self.get_queryset()
          serializer = self.get_serializer(queryset)
          if not queryset:
              return self.response_notfound('Task')
          return self.response_ok(serializer.data)

      def put(self,request,pk):
          queryset = self.get_queryset()
          if not queryset:
              return self.response_notfound('Task')
          serializer = self.get_serializer(queryset,data=request.data,context={'tenant_id':request.user.tenant.id},partial=True)
          serializer.is_valid(raise_exception=True)
          serializer.save(updated_by=request.user)
          return self.response_ok(serializer.data,'Task updated')

      def delete(self,request,pk):
          queryset = self.get_queryset()
          task = self.get_queryset()
          if not queryset:
              return self.response_notfound('Task')
          queryset.delete()
          return self.response_archived(f'Task: {task.title}')
