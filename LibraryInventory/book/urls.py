from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('catalog/', views.CatalogView.as_view(), name='catalog'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('details/<int:pk>', views.DetailsView.as_view(), name='details'),
]