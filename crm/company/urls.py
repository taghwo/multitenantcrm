from django.urls import path
from .views import ListCreateCompany, ShowUpdateDeleteCompany
urlpatterns = [
    path("",ListCreateCompany.as_view(), name='list_create_company'),
    path("/<int:pk>",ShowUpdateDeleteCompany.as_view(), name='show_update_delete_company')
]
