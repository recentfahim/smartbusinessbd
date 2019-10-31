from django.urls import path, include
from . import views

urlpatterns = [
    path('category/', views.GetCategory.as_view(), name='get_category')
]
