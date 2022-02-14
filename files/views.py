from curses.ascii import US
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import CreateView,ListView
from django.views.generic.edit import FormView
from account.models import User
from .forms import UploadFileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import FileModel,VideoModel,ImageModel
# Create your views here.

class HomeView(FormView):
    template_name = "files/index.html"
    form_class = UploadFileForm

    def form_valid(self, form):
        print(form.cleaned_data['text'])
        user = self.request.user
        #file 
        if self.request.FILES['file']:
            file = self.request.FILES['file']
            if file.content_type[:5] == 'video':
                type = 'video'
                new_record = VideoModel(user = user,file = file,text = form.cleaned_data['text'])
            elif file.content_type[:5] == 'image':
                type = 'image'
                new_record = ImageModel(user = user,file = file,text = form.cleaned_data['text'])
            
            messages.success(self.request,f'Your {type} Uploaded Successfully ')    
            new_record.save()
        return redirect('/')
    
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            Video = VideoModel.objects.filter(user = self.request.user).order_by('time').last()
            context['videos'] = Video

            Image = ImageModel.objects.filter(user = self.request.user).order_by('time').last()
            context['images'] = Image
        return context



class VideoView(ListView):
    template_name = 'files/video.html'
    is_video = False
    

    def get_queryset(self):
        query = VideoModel.objects.filter(user = self.request.user)
        return query