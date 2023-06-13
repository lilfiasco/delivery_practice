from django.forms.models import BaseModelForm
from django.http import HttpResponseRedirect
from django.db import models
from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from main import forms, models
from auths import models as a_models
from django.db.models import Count
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView, 
    View, 
    DetailView,
    UpdateView
)
from django.views.decorators.csrf import csrf_exempt


def get_base(request) -> HttpResponse:
    form = AuthenticationForm
    return render (request, 'base.html', context={ 'form': form })

def get_index(request) -> HttpResponse:
    form = AuthenticationForm
    return render (request, 'index.html', context={ 'form': form })

def get_menu(request) -> HttpResponse:
    form = forms.FoodForm
    return render (request, 'food/menu.html', context={ 'form': form })

def get_cart(request) -> HttpResponse:
    return render (request, 'orders/cart.html')

def get_cart2(request) -> HttpResponse:
    return render (request, 'orders/cart2.html')

def test(request) -> HttpResponse:
    return render (request, 'orders/test.html')

@csrf_exempt
def test_ajax(request):
    print("DDDDDD: ", request.POST)
    return JsonResponse({'success': True}, safe=False)


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
        context['selected_category'] = category_title  # Pass selected category to template
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
    

class MenuFranchiseView(ListView):
    model = models.Food
    template_name = 'food/menu_franchise.html'
    context_object_name = 'food'

    def get_queryset(self):
        queryset = super().get_queryset()

        franchise_id = self.kwargs.get('franchise_id')
        franchise = get_object_or_404(models.Franchise, id=franchise_id)
        
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__slug=category)
        
        return queryset.filter(franchise=franchise)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        franchise_id = self.kwargs.get('franchise_id')
        franchise = get_object_or_404(models.Franchise, id=franchise_id)
        context['franchise'] = franchise

        return context
    
    
class MenuFranchiseView2(ListView):
    model = models.Food
    template_name = 'food/menu_franchise2.html'
    context_object_name = 'food'

    def get_queryset(self):
        queryset = super().get_queryset()

        franchise_id = self.kwargs.get('franchise_id')
        franchise = get_object_or_404(models.Franchise, id=franchise_id)
        
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__title=category)
        
        return queryset.filter(franchise=franchise)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        franchise_id = self.kwargs.get('franchise_id')
        franchise = get_object_or_404(models.Franchise, id=franchise_id)
        context['franchise'] = franchise
        context['selected_category'] = self.request.GET.get('category')
        non_empty_categories = models.Category.objects.filter(food__franchise=franchise).annotate(food_count=Count('food')).filter(food_count__gt=0)
        context['non_empty_categories'] = non_empty_categories

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
        food = models.Food.objects.get(slug=slug)

        return render(request, 'food/food_detail.html', {"food": food})
    