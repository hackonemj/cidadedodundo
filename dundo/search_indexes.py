import datetime
from haystack import indexes
from dundo.models import Noticia


class NoticiaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    titulo = indexes.CharField(model_attr='titulo')
    noticia_texto = indexes.CharField(model_attr='noticia_texto')
    publish = indexes.DateTimeField(model_attr='publish')

    def get_model(self):
        return Noticia

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(publish__lte=datetime.datetime.now())