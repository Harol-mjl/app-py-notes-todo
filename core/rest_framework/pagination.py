from rest_framework import pagination

class OptionalPageNumberPagination(pagination.PageNumberPagination):
    page_size = 10

    def paginate_queryset(self, queryset, request, view=None):
        query_params_lower = {k.lower(): v for k, v in request.query_params.items()}
        query_param_pagination = query_params_lower.get("pagination")

        self.page_size = query_params_lower.get("pagesize") or query_params_lower.get("page_size") or self.page_size
        if query_param_pagination and query_param_pagination.strip().lower() == 'false':
            return None
        return super().paginate_queryset(queryset, request, view)
