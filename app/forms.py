from django.forms import ModelForm
from .models import Profile, Experience, Project, Certificate,TechnicalSkill,SoftSkill

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'description']


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']


class TechnicalSkillForm(ModelForm):
    class Meta:
        model = TechnicalSkill
        fields = ['name']

class SoftSkillForm(ModelForm):
    class Meta:
        model = SoftSkill
        fields = ['name']


class CertificateForm(ModelForm):
    class Meta:
        model = Certificate
        fields = ['name']
