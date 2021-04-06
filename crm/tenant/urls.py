from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.ListCreateTenant.as_view(), name="list_create_tenant"),
    path("/detail", views.ShowUpdateDeleteTenant.as_view(), name="show_update_delete")
]
