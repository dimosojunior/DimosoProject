from DimosoApp.models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class MyUserForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Required. Add a valid email address.")
    
    

    class Meta:
        model = MyUser
        fields = (
        "email",
        "username",
        "password1",
        "password2"

        
         )
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            myuser = MyUser.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} is already exist.")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            myuser = MyUser.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"username {username} is already exist.")

         



         
        
class UserLoginForm(forms.ModelForm):
    password=forms.CharField(
        
        widget = forms.PasswordInput(attrs={'placeholder':'password', 'class':'input'})

    ) 
    email=forms.CharField(
        
        widget = forms.EmailInput(attrs={'placeholder':'email', 'class':'input'})

    )  

    class Meta:
        model=MyUser
        fields=('email', 'password')

    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            password=self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError("username or password incorrect")

class PostForm(forms.ModelForm):

    
    name = forms.CharField(
            label=False,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder' : 'Enter Post Name'})
      
       )
    title_tag = forms.CharField(
            label=False,
            required=False,
            
            widget=forms.TextInput(attrs={'id' :'title_tag','class': 'inputi', 'placeholder' : 'Enter Title Tag'})
      
       )
    class Meta:
        model = Post
        fields = '__all__'


class UploadFilesForm(forms.ModelForm):

    name = forms.CharField(
            label=False,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder': "SEARCH A PDF NOTES"})
      
       )
    
      
       
    class Meta:
        model = UploadFiles
        fields = '__all__'

class MyDocumentsForm(forms.ModelForm):

    name = forms.CharField(
            label=False,
            widget=forms.TextInput(attrs={'id' :'name', 'placeholder': "SEARCH A PDF Documents"})
      
       )
    
      
       
    class Meta:
        model = MyDocuments
        fields = '__all__'




class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '4',
            'id': 'content',
            'placeholder' : 'Write your Comment for this tutorial',
        }))
    class Meta:
        model = Comment
        fields = ('content',)