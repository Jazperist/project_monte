from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import ClienteCreateForm
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view


"""
# Create your views here.
def home(request):
  context = {"name": "Amigo"}
  return render(request, "montepiadoso/home.html", context)

class ClienteList(generics.ListCreateAPIView):
  queryset = Cliente.objects.all()
  serializer_class = ClienteSerializer
  template_name = "montepiadoso/cliente_create_form.html"
"""

class ClienteList(LoginRequiredMixin, ListView):
   model = Cliente
   template_name = "montepiadoso/cliente_list.html"

class ClienteCreate(CreateView):
  model = Cliente
  template_name = "montepiadoso/cliente_create_form.html"
  form_class = ClienteCreateForm

class ClienteUpdate(LoginRequiredMixin, UpdateView):
  model = Cliente
  template_name = "montepiadoso/cliente_update_form.html"
  fields = ["nombre", "apellido", "telefono", "email", "cantidad_pedida", "plazo"]
  success_url = "/cliente/list"

class ClienteDelete(LoginRequiredMixin, DeleteView):
  model = Cliente
  template_name = "montepiadoso/cliente_delete_form.html"
  success_url = "/cliente/list"



def login_view(request):
    context = {
        "login_view": "active"
    }
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("clientelist")
        else:
            return HttpResponse("invalid credentials")
    return render(request, "registration/login.html", context)

def logout_view(request):
    logout(request)
    return redirect("login")

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@api_view(['GET', 'POST'])
def clientes_list(request):
    if request.method == 'GET':
        data = Cliente.objects.all()

        serializer = ClienteSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def clientes_detail(request, pk):
    try:
        cliente = Cliente.objects.get(pk=pk)
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ClienteSerializer(cliente, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
