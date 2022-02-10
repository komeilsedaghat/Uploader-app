from django import forms
from .models import FileModel

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields= '__all__'

    def __init__(self,*args,**kwawrgs):
        super(UploadFileForm,self).__init__(*args,**kwawrgs)
        self.fields['file'].widget.attrs = {'class':'','hidden':'','id':'file'}
