from django.views.generic import ListView
from dummy.models import Article


class Index(ListView):
    model = Article


index = Index.as_view()
