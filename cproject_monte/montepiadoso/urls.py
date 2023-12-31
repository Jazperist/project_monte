from django.urls import path, re_path
from . import views

urlpatterns = [
    #path('', views.home, name="home"),
    path("cliente/list", views.ClienteList.as_view(), name="clientelist"),
    path("", views.ClienteCreate.as_view(), name="clientecreate"),
    path("cliente/update/<pk>", views.ClienteUpdate.as_view(), name="clienteupdate"),
    path("cliente/delete/<pk>", views.ClienteDelete.as_view(), name="clientedelete"),
    #path('cliente/list', views.ClienteList.as_view(), name="clientelist"),
    #path('cliente/create', views.ClienteList.as_view(), name="clientecreate"),
    path("accounts/login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    re_path(r'^api/clientes/$', views.clientes_list),
    path('api/clientes/<pk>', views.clientes_detail),
]