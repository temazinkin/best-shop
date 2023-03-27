from django.urls import path
from shop.views import category_view

urlpatterns = [
    path('all/<slug:url>/', category_view, name='category'),
]
