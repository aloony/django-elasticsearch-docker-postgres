# from haystack import indexes
# from mainapp.models import Movie

# class MovieIndex(indexes.SearchIndex, indexes.Indexable):
#     description = indexes.CharField(document=True, use_template=True, template_name="search/book_text.txt")
#     title = indexes.CharField(model_attr='title')
#     director = indexes.CharField()

#     def get_model(self):
#         return Movie

#     def index_queryset(self, using=None):
#         return self.get_model().objects.all()