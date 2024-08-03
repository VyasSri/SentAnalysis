from django.forms import ModelForm
from django import forms
from .models import signup_info, FormData, AnalyzeData
from django.contrib.auth.forms import UserCreationForm

class signup_form(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

    class Meta:
        model = signup_info
        fields = ('username', 'email', 'password1', 'password2')

# sentAI/forms.py


class SubmissionForm(ModelForm):
    class Meta:
        model = FormData
        fields = ['subject', 'content', 'sentiment']


class SentimentForm(ModelForm):
    class Meta:
        model = AnalyzeData
        fields = ['email_subject', 'email_content']