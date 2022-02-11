from django import forms
from .models import FileModel, VideoModel

class UploadFileForm(forms.Form):
    file = forms.FileField(required=True,widget=forms.FileInput(attrs={'id':'file','hidden':''}))
    text = forms.CharField(max_length=200,required=False,widget=forms.Textarea(attrs={'class':'text-plan bg-info','rows':'1'}))


    def clean_file(self):
        file = self.cleaned_data['file']
        size = file.size
        max_size = 100000000

        if size > max_size:
            raise forms.ValidationError('Your Uploaded File Mose Be Less Then 100 MB')
        else:
            pass