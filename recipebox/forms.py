from django import forms
from recipebox.models import Author, Recipe

class AuthorAddForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)

class RecipeAddForm(forms.ModelForm):
    class Meta:
            model = Recipe
            fields = ['author', 'title', 'description', 'time_required', 'instructions']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)