from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class BasePaginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1
    def get_paginated_response(self, data):
        return Response({
            'next':self.get_next_link(),
            'previous':self.get_previous_link(),
            'total':self.page.paginator.count,
            'current_page':self.page.number,
            'data':data
        })
