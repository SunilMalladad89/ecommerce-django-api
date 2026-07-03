from django.urls import path
from . import views

app_name= 'products'

# urlpatterns = [
#     path('products/', views.product_list, name="product-list"),
#     path('products/<int:id>/',views.product_details, name='product-details'),
#     path('products/create/', views.product_create, name='product-create'),
#     path('products/<int:id>/update/', views.product_update, name='product-update'),
#     path('products/<int:id>/delete/', views.product_delete , name='product-delete'),
# ]

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-details'),
    path('products/create/', views.ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
]