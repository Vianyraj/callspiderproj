import django_filters
from .models import Bmbf_model, Wiki_model

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Wiki_model
        fields= { 'Title': ['icontains'],
                  #'Dates': ['icontains'],
                  'Url' :  ['icontains'],
                  'Where': ['icontains'],
                  #'Deadline': ['icontains'],
                }

class OrderFilter1(django_filters.FilterSet):
            class Meta:
                model = Bmbf_model
                fields = {'Title': ['icontains'],
                          #'Dates': ['icontains'],
                          'Url': ['icontains'],
                          #'Deadline': ['icontains'],
                          }