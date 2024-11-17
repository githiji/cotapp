from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("index/", views.IndexView.as_view(), name="index"),
    path('create/', views.add_stock, name='create'),
    path('cot/', views.COTReportListView.as_view(), name='cot'),
]

