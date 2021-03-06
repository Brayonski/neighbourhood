from django import forms
from .models import Neighbourhood,Business,Posts,Profile,Comment
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['user']

class CreateBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name','neighbourhood','image','email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class AddCommunityForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['user']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','neighbourhood']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
