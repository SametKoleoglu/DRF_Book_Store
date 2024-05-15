from rest_framework.pagination import PageNumberPagination


class SmallPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'


class LargePagination(PageNumberPagination):
    page_size = 20
    page_query_param = 'page_size'
