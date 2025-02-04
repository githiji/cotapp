from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("index/", views.IndexView.as_view(), name="index"),
    path('create/', views.add_stock, name='create'),
    path('cot/', views.view_cot, name='cot'),
    path('symbol/<int:id>/', views.symbol, name='symbol')
]

