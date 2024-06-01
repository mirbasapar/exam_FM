from django.urls import path
from .views import HomeView, ProductListView, ProductDetailView, AddReviewView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<str:category>/', ProductListView.as_view(), name='product_list_by_category'),
    path('products/detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/detail/<int:pk>/add_review/', AddReviewView.as_view(), name='add_review'),
]
