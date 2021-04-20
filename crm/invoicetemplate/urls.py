from invoicetemplate.views import ListCreateInvoiceTemplate, ShowUpdateDeleteInvoiceTemplate
from django.urls import path

urlpatterns = [
     path("",ListCreateInvoiceTemplate.as_view(), name='list_create_invoce_template'),
     path("/<uuid:pk>",ShowUpdateDeleteInvoiceTemplate.as_view(), name='show_update_delete_invoice_template')
]