from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ClienteCreateForm
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework import generics

# Create your views here.
def home(request):
  context = {"name": "Amigo"}
  return render(request, "montepiadoso/home.html", context)

class ClienteList(generics.ListCreateAPIView):
  queryset = Cliente.objects.all()
  serializer_class = ClienteSerializer


#class ClienteList(ListView):
#   model = Cliente
#   template_name = "montepiadoso/cliente_list.html"

class ClienteCreate(CreateView):
  model = Cliente
  template_name = "montepiadoso/cliente_create_form.html"
  form_class = ClienteCreateForm

class ClienteUpdate(UpdateView):
  model = Cliente
  template_name = "montepiadoso/cliente_update_form.html"
  fields = ["nombre", "apellido", "telefono", "email", "cantidad_pedida", "plazo"]
  success_url = "/cliente/list"

class ClienteDelete(DeleteView):
  model = Cliente
  template_name = "montepiadoso/cliente_delete_form.html"
  success_url = "/cliente/list"
