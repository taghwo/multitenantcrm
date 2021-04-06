from django.urls import path
from .views import ListCreateTask, ShowUpdateDeleteTask
urlpatterns = [
    path("",ListCreateTask.as_view(), name='list_create_task'),
    path("/<int:pk>",ShowUpdateDeleteTask.as_view(), name='show_update_delete_task')
]
