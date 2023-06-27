from django.forms.models import BaseModelForm
from django.http import HttpResponseRedirect,JsonResponse
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from main import forms, models
from auths import models as a_models
import json
from django.db.models import Count, Q
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView, 
    View, 
    DetailView,
    UpdateView
)
from django.core import serializers
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
import json

from django.core import serializers

from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
import json
import random

class RecommendationView(View):
    def get(self, request):
        return render(request, 'orders/get_gart.html')
    def post(self, request):
        cart_data = request.POST.get('cartData')
        cart_data = json.loads(cart_data)  # Convert JSON string to Python object
        food_ids = cart_data.keys()
        franchise_id = models.Food.objects.filter(id__in=food_ids).values_list('franchise_id', flat=True).first()
        cluster_ids = models.Food.objects.filter(id__in=food_ids).values_list('cluster', flat=True).distinct()
        recommended_food = models.Food.objects.filter(
            franchise_id=franchise_id,
            cluster__in=cluster_ids,
        ).exclude(id__in=food_ids)
        recommended_food = list(recommended_food)
        random.shuffle(recommended_food)
        paginator = Paginator(recommended_food, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        recommended_food_data = []
        for food in page_obj:
            food_data = {
                'id': food.id,
                'title': food.title,
                'price': food.price,
                'quantity': food.quantity,
                'image': food.image.url,
            }
            recommended_food_data.append(food_data)
        context = {
            'recommended_food': recommended_food_data,
            'page_obj': {
                'number': page_obj.number,
                'paginator': {
                    'num_pages': page_obj.paginator.num_pages
                }
            }
        }
        response_data = json.dumps(context)
        return HttpResponse(response_data, content_type='application/json')


def get_base(request) -> HttpResponse:
    form = AuthenticationForm
    return render (request, 'base.html', context={ 'form': form })

def get_index(request) -> HttpResponse:
    form = AuthenticationForm
    return render (request, 'index.html', context={ 'form': form })

def get_menu(request) -> HttpResponse:
    form = forms.FoodForm
    return render (request, 'food/menu.html', context={ 'form': form })

# def get_cart(request) -> HttpResponse:
#     franchise = models.Franchise.objects.all()
#     return render(request, 'orders/cart.html', context={'franchise': franchise})
def get_cart(request):
    franchise_id = request.POST.get('franchiseId')
    print(franchise_id)
    franchise = models.Franchise.objects.filter(id=franchise_id).first()
    return render(request, 'orders/cart.html', {'franchise': franchise})



def get_cart2(request) -> HttpResponse:
    return render (request, 'orders/cart2.html')

class CreateFoodView(CreateView):
    """
    Add new food.
    """

    form_class = forms.FoodForm
    success_url = reverse_lazy('create_food')
    template_name = 'food/add_food.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['franchise'] = a_models.Coworker.objects.get(pk=self.request.user.id).franchise
        context['food'] = models.Food.objects.all()
        print('FFFFFFFFF: ', context)
        print('AAAAAAAAAAAA:', context['franchise'])
        return context

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        print("AZAZAZA: ", form.errors)
        return super().form_invalid(form)

    def form_valid(self, form): 
        try:
            food = form.save(commit=False)
            food.save()
            print("sssssssssssss" ,food)
            return render(self.request, 'food/add_food_success.html')
        except ValueError as e:
            form.add_error('image', str(e))  
            return self.form_invalid(form)
        

class FranchiseListView(ListView):
    model = models.Franchise
    template_name = 'food/franchise_list.html'
    context_object_name = 'franchises'
    paginate_by = 6


class MenuView(TemplateView):
    template_name = 'food/menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_title = self.request.GET.get('category')
        food = models.Food.objects.all()

        if category_title:
            food = food.filter(category__title=category_title)

        categories = models.Category.objects.annotate(food_count=Count('food')).filter(food_count__gt=0)
        context['food'] = food
        context['categories'] = categories
        context['selected_category'] = category_title  
        return context



class FranchiseDetailView(DetailView):
    pass
    paginate_by = 3 
    model = models.Franchise
    template_name = 'food/franchise_detail.html'
    context_object_name = 'franchise'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        franchise = self.get_object()
        category_title = self.request.GET.get('category')
        food = franchise.food_set.all() 
        if category_title:
            food = food.filter(category__title=category_title)
        categories = models.Category.objects.all()
        context['food_list'] = food
        context['categories'] = categories
        context['selected_category'] = category_title
        return context
    





# class MenuFranchiseView(ListView):
#     model = models.Food
#     template_name = 'food/menu_franchise.html'
#     context_object_name = 'food'

#     def get_queryset(self):
#         queryset = super().get_queryset()

#         franchise_id = self.kwargs.get('franchise_id')
#         franchise = get_object_or_404(models.Franchise, id=franchise_id)
        
#         category = self.request.GET.get('category')
#         if category:
#             queryset = queryset.filter(category__slug=category)
        
#         return queryset.filter(franchise=franchise)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         franchise_id = self.kwargs.get('franchise_id')
#         franchise = get_object_or_404(models.Franchise, id=franchise_id)
#         context['franchise'] = franchise

#         return context
class MenuFranchiseView(ListView):
    template_name = 'food/menu_franchise_new.html'
    context_object_name = 'categories'

    def get_queryset(self):
        franchise_id = self.kwargs.get('franchise_id')
        return models.Category.objects.filter(food__franchise_id=franchise_id).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        franchise_id = self.kwargs.get('franchise_id')
        search_query = self.request.GET.get('search', '')
        selected_category = self.request.GET.get('category')

        categories = context['categories'].filter(food__franchise_id=franchise_id).distinct()
        filtered_categories = []

        for category in categories:
            filtered_foods = category.food_set.filter(franchise_id=franchise_id)
            if search_query:
                filtered_foods = filtered_foods.filter(
                    Q(title__icontains=search_query) |
                    Q(category__title__icontains=search_query)
                )
            if selected_category and selected_category != category.title:
                filtered_foods = filtered_foods.none()
            if filtered_foods.exists():
                filtered_categories.append((category, filtered_foods))

        context['filtered_categories'] = filtered_categories
        context['franchise'] = models.Franchise.objects.get(id=franchise_id)
        context['search_query'] = search_query
        context['selected_category'] = selected_category
        return context    
    
class MenuFranchiseView2(ListView):
    template_name = 'food/menu_franchise2.html'
    context_object_name = 'categories'

    def get_queryset(self):
        franchise_id = self.kwargs.get('franchise_id')
        return models.Category.objects.filter(food__franchise_id=franchise_id).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        franchise_id = self.kwargs.get('franchise_id')
        search_query = self.request.GET.get('search', '')
        selected_category = self.request.GET.get('category')

        categories = context['categories'].filter(food__franchise_id=franchise_id).distinct()
        filtered_categories = []

        for category in categories:
            filtered_foods = category.food_set.filter(franchise_id=franchise_id)
            if search_query:
                filtered_foods = filtered_foods.filter(
                    Q(title__icontains=search_query) |
                    Q(category__title__icontains=search_query)
                )
            if selected_category and selected_category != category.title:
                filtered_foods = filtered_foods.none()
            if filtered_foods.exists():
                filtered_categories.append((category, filtered_foods))

        context['filtered_categories'] = filtered_categories
        context['franchise'] = models.Franchise.objects.get(id=franchise_id)
        context['search_query'] = search_query
        context['selected_category'] = selected_category
        return context   


class FranchiseFoodEditView(UpdateView):
    model = models.Food
    template_name = 'food/franchise_food_edit.html'
    context_object_name = 'franchise'
    fields = ['title', 'description', 'price','franchise', 'image']
    
    def get_object(self):
        return self.model.objects.get(slug=self.kwargs.get('slug'))
    
    def post(self, request, *args, **kwargs):
        if 'delete' in request.POST:
            obj = self.get_object()
            franchise = obj.franchise.pk
            self.get_object().delete()
            return HttpResponseRedirect(reverse_lazy('franchise_detail', kwargs={'pk': franchise}))
        return super().post(request, *args, **kwargs)
        
    def get_success_url(self):
        return reverse_lazy('franchise_detail', kwargs={'pk': self.object.franchise.pk, })


class FoodDetailView(View):
    def get(self, request, slug):
        print("FFFFFFFF:", slug)
        food = models.Food.objects.get(slug=slug)

        return render(request, 'food/food_detail.html', {"food": food})
    




# class FranchiseOrdersListView(ListView):
#     model = a_models.Purchase
#     template_name = 'food/franchise_purchase.html'
#     context_object_name = 'purchases'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         franchise_id = self.kwargs['franchise_id']
#         purchases = a_models.Purchase.objects.filter(franchise_id=franchise_id)
#         context['purchases'] = purchases

#         # Get the food titles and images for the corresponding food IDs
#         food_data = models.Food.objects.filter(franchise_id=franchise_id).values('id', 'title', 'image')
#         food_dict = {food['id']: {'title': food['title'], 'image': food['image']} for food in food_data}

#         # Preprocess the order items to include food titles and images
#         for purchase in purchases:
#             order_items = purchase.order
#             for item in order_items:
#                 food_id = item['food_id']
#                 food_info = food_dict.get(food_id)
#                 if food_info:
#                     item['food_title'] = food_info['title']
#                     item['food_image'] = food_info['image']

#         return context



class FranchiseOrdersListView(ListView):
    model = a_models.Purchase
    template_name = 'food/franchise_purchase.html'
    context_object_name = 'purchases'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        franchise_id = self.kwargs['franchise_id']
        purchases = a_models.Purchase.objects.filter(franchise_id=franchise_id)
        context['purchases'] = purchases

        # Get the food titles and images for the corresponding food IDs
        food_data = models.Food.objects.filter(franchise_id=franchise_id).values('id', 'title', 'image')
        food_dict = {food['id']: {'title': food['title'], 'image': food['image']} for food in food_data}

        # Preprocess the order items to include food titles and images
        for purchase in purchases:
            order_items = purchase.order
            total_price = 0  # Initialize total price for each purchase
            for item in order_items:
                food_id = item['food_id']
                food_info = food_dict.get(food_id)
                if food_info:
                    item['food_title'] = food_info['title']
                    item['food_image'] = food_info['image']
                    total_price += item['total_price']  # Accumulate total price

            purchase.total_price = total_price  # Add total price to purchase object

        return context



