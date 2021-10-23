from invoice.views import ListCreateInvoice, ShowUpdateDeleteInvoice
from django.urls import path

urlpatterns = [
     path("",ListCreateInvoice.as_view(), name='list_create_invoce'),
     path("/<uuid:pk>",ShowUpdateDeleteInvoice.as_view(), name='show_update_delete_invoice')
]