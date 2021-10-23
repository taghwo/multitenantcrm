from django.urls import path
from .views import ListCreateFeedback,RetrieveDeleteFeedback
urlpatterns = [
    path("", ListCreateFeedback.as_view(),name="list_create_feedback"),
    path("/<int:pk>", RetrieveDeleteFeedback.as_view(),name="view_delete_feedback")
]