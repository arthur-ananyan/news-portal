from django.urls import path
from .views import home, category_list, category_selected, news_details

urlpatterns = [
    path('', home, name="home"),
    path('categories/', category_list, name="category"),
    path('categories/<str:category_name>/', category_selected,
         name="category_selected"),
    path('details/<int:pk>/', news_details, name="details"),
]
