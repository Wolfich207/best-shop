from django.urls import path
from shop.views import (
    category_view,
    product_view,
)

urlpatterns = [
    path('all/<slug:url>/', category_view, name='category'),
    path('<slug:url>/', product_view, name='product'),
]
