import django_filters
from main import models
class FoodFilter(django_filters.FilterSet):
    category__title = django_filters.CharFilter(field_name='category__title', lookup_expr='exact')

    class Meta:
        model = models.Food
        fields = ['category__title']
