from django.views.generic import ListView
from dummy.models import Article


class Index(ListView):
    model = Article


class RaiseException(ListView):
    model = Article

    def dispatch(self, *args, **kwargs):
        raise Exception


index = Index.as_view()
raise_exception = RaiseException.as_view()
