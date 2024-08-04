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
        widgets = {
            'subject': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Subject', 'readonly': 'readonly'}),
            'content': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Content', 'readonly': 'readonly'}),
            'sentiment': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Sentiment', 'readonly': 'readonly'}),
        }


class SentimentForm(ModelForm):
    class Meta:
        model = AnalyzeData
        fields = ['email_subject', 'email_content']
        widgets = {
            'email_subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'email_content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}),
        }