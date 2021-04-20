from transaction.views import ListCreateTransaction, ShowUpdateDeleteTransaction
from django.urls import path

urlpatterns = [
     path("",ListCreateTransaction.as_view(), name='list_create_transaction'),
     path("/<uuid:pk>",ShowUpdateDeleteTransaction.as_view(), name='show_update_delete_transaction')
]