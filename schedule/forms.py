from django import forms
from .models import Student


class SearchForm(forms.Form):
    q = forms.CharField(max_length=200, label="Search by the name")


class ApplyCourseForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"