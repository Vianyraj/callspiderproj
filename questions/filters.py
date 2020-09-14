import django_filters
from .models import Paper_model
class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Paper_model
        fields=( 'Title', 'PaperType','Where',)