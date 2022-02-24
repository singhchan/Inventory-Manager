from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import widgets
from main import models 

class EmployeeCreationForm(forms.ModelForm):
    department = forms.ChoiceField(widget=forms.Select(), choices=models.Employee().DEPARTMENT)
    gender = forms.ChoiceField(widget=forms.Select(), choices=models.Employee().GENDER)
    class Meta:
        model = models.Employee
        fields = ['name', 'department', 'gender', 'age']

class UpdateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class UpdateEmployee(forms.ModelForm):
    department = forms.ChoiceField(widget=forms.Select(), choices=models.Employee().DEPARTMENT)
    gender = forms.ChoiceField(widget=forms.Select(), choices=models.Employee().GENDER)
    class Meta:
        model = models.Employee
        exclude = ['id']

class UpdatePossesion(forms.ModelForm):
    class Meta:
        model = models.Possesion
        fields = '__all__'
        widgets = {
            'issueraised': forms.CheckboxInput(),
        }