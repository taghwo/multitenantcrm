from django.urls import path
from .views import ListCreateContact,ShowUpdateDelete
urlpatterns = [
    path("",ListCreateContact.as_view(),name="list-create-contact"),
    path("/<int:pk>",ShowUpdateDelete.as_view(),name="show-update-delete-contact")
]