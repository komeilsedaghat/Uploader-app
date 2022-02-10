from django.shortcuts import render
from django.views.generic import ListView,DetailView,FormView
from .forms import UploadFileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import FileModel
# Create your views here.

class HomeView(FormView):
    template_name = "files/index.html"
    form_class = UploadFileForm

