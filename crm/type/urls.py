from django.urls import path
from .views import ListCreateClientType, ShowUpdateDeleteClientType
urlpatterns = [
    path("",ListCreateClientType.as_view(), name='list_create_type'),
    path("/<int:pk>",ShowUpdateDeleteClientType.as_view(), name='show_update_delete_type')
]
