from django import forms
from Django_SRIT.models import uploadfolder

class uploadfileform(forms.ModelForm):
    class Meta:
        model=uploadfolder
        fields=('File_to_upload',)