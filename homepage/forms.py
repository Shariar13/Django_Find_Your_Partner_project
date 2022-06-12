from django import forms
from django.contrib.auth.forms import UserChangeForm
from.models import profile
from.models import post



class edit_profile_form(forms.ModelForm):

    height=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    weight=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    eyes=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    hair=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    education=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    phone=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    description=forms.CharField(max_length=1000,widget=forms.TextInput(attrs={'class':'form-control'}))
    profile_pic=forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))
    cover_pic=forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))
    

    

    class Meta:
        model = profile
        fields = ('height', 'weight', 'eyes', 'hair', 'education', 'phone', 'email', 'description','profile_pic', 'cover_pic')



class edit_post_form (forms.ModelForm):

    status=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = post
        fields = ('status',)