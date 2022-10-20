from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name = 'index'),
    # path('detail/<int:tech_pk>/', views.detail_tech, name='detail_tech'),
    # path('detail/<int:company_pk>/', views.detail_company, name='detail_company'),
]
