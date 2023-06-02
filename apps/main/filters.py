import django_filters
from main import forms, models
from auths import forms as a_forms, models as a_models
# from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _
# from PIL import Image

class FoodFilter(django_filters.FilterSet):
    category__title = django_filters.CharFilter(field_name='category__title', lookup_expr='exact')

    class Meta:
        model = models.Food
        fields = ['category__title']
