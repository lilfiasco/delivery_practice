from django.urls import path
from . import views
from apps.main.views import(
    get_base,
    get_index,
    get_menu,
    get_cart,
    CreateFoodView,
    MenuView,
    
    FranchiseDetailView,
    FoodDetailView,
    FranchiseFoodEditView,
    cart_view,
    FranchiseListView,
    MenuFranchiseView,

)


urlpatterns = [
    path('base/', get_base),
    path('cart/', get_cart, name='cart'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('menu/<slug:slug>/', FoodDetailView.as_view(), name="menu_object"),
    
    path('', get_index,name='index'),
    path('check_food/', CreateFoodView.as_view(), name='create_food'),
    path('franchise/', FranchiseListView.as_view(), name='franchise'),
    path('franchise/<int:franchise_id>/',MenuFranchiseView.as_view(), name='menu_franchise'),
    path('/franchise/<int:pk>/edit', FranchiseDetailView.as_view(), name='franchise_detail'),
    path('<slug:slug>/', FoodDetailView.as_view(),name="food_slug" ),
    path('franchise/<int:pk>/<slug:slug>/', FranchiseFoodEditView.as_view(),name="food_edit" ),

]

