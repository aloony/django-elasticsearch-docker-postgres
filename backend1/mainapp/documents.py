from django_elasticsearch_dsl import Document, fields
from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl.registries import registry
from .models import Movie

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

@registry.register_document
class MovieDocument(Document):

    class Index:
        name = 'movies'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
    
    class Django:
        model = Movie

        fields = [
            'title',
            'director',
            'description'
        ]





