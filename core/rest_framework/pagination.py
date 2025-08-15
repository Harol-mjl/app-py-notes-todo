from rest_framework import pagination

class OptionalPageNumberPagination(pagination.PageNumberPagination):
    page_size = 10

    def paginate_queryset(self, queryset, request, view=None):
        query_params = request.query_params
        self.page_size = query_params.get("pagesize") or query_params.get("page_size") or self.page_size
        if request.query_params.get("pagination") == "false":
            return None
        return super().paginate_queryset(queryset, request, view)
