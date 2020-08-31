from django import forms
from .models import CVpost, Projects, Qualifications

class CVForm(forms.ModelForm):

    class Meta:
        model = CVpost
        fields = ('homeAddress', 'email', 'contactNumber', 'status', 'aboutMe')

class ProjectsForm(forms.ModelForm):

    class Meta:
        models = Projects
        fields = ('projectTitle', 'projectDescription')

class QualificationsForm(forms.ModelForm):

    class Meta:
        model = Qualifications
        fields = ('qualification',)
