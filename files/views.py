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
        user = self.request.user
        #file 
        if self.request.FILES['file']:
            file = self.request.FILES['file']
            if file.content_type[:5] == 'video':
                new_record = VideoModel(user = user,file = file)
            elif file.content_type[:5] == 'image':
                new_record = ImageModel(user = user,file = file)
                
            new_record.save()
        
        return redirect('/')


class VideoView(ListView):
    template_name = 'files/video.html'
    is_video = False
    

    def get_queryset(self):
        query = FileModel.objects.filter(user = self.request.user)
        for qu in query:
            print(qu.file)
            # if qu.file.content_type[:5] == 'video':
            #     return qu