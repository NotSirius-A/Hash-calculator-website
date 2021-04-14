from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.calculator_page_view, name='calculator_page_view')
]
