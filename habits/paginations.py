<<<<<<< HEAD
from rest_framework.pagination import PageNumberPagination


class PagePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 50
=======
from rest_framework.pagination import PageNumberPagination


class PagePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 50
>>>>>>> b06ae89223852ac8726da1a522d7e09db2c8c7e7
