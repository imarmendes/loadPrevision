from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['projectName', 'responsible', 'address', 'art']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['responsible'].required = False
        self.fields['address'].required = False
        self.fields['art'].required = False