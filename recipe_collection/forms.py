from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Recipe


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Profile
        fields = ['email', 'bio']  
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        self.instance.user.email = self.cleaned_data['email']
        self.instance.user.save()
        return super().save(commit)


class RecipeForm(forms.ModelForm):
    ingredients = forms.CharField(widget=forms.Textarea)
    preparation = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Recipe
        fields = ['headline', 'description', 'ingredients', 'preparation', 'image']