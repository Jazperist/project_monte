from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    #path("cliente/list", views.ClienteList.as_view(), name="clientelist"),
    path("cliente/create", views.ClienteCreate.as_view(), name="clientecreate"),
    path("cliente/update/<pk>", views.ClienteUpdate.as_view(), name="clienteupdate"),
    path("cliente/delete/<pk>", views.ClienteDelete.as_view(), name="clientedelete"),
    path('cliente/api', views.ClienteList.as_view(), name="clienteList")
]