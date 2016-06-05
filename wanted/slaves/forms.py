from django import forms
from . import models



class FormAddSlaveView(forms.ModelForm):
    #https://docs.djangoproject.com/en/1.9/ref/models/fields/
    #https://godjango.com/35-upload-files/
    model = models.Slave
    fields = ['fname']
    exclude = (
     #   'user',
    )