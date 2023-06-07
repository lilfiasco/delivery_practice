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
    MenuFranchiseView2,

    )


from apps.auths.views import OrderCreateViewSet


urlpatterns = [
    path('base/', get_base),
    path('cart/', get_cart, name='cart'),
    path('menu/', MenuView.as_view(), name='menu'),

    path('order/', OrderCreateViewSet.as_view({'get': 'list', 'post': 'create'})),  
    path('menu/<slug:slug>/', FoodDetailView.as_view(), name="menu_object"),
    
    path('', get_index,name='index'),
    path('check_food/', CreateFoodView.as_view(), name='create_food'),
    path('franchise/', FranchiseListView.as_view(), name='franchise'),
    path('franchises/<int:franchise_id>/',MenuFranchiseView.as_view(), name='menu_franchise'),
    
    path('franchise/<int:franchise_id>/',MenuFranchiseView2.as_view(), name='menu_franchise2'),
    path('/franchise/<int:pk>/edit', FranchiseDetailView.as_view(), name='franchise_detail'),
    path('<slug:slug>/', FoodDetailView.as_view(),name="food_slug" ),
    
    # Коворкер редачит
    path('franchise/<int:pk>/<slug:slug>/', FranchiseFoodEditView.as_view(),name="food_edit" ),

]

