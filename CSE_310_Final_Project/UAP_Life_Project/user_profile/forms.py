from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account, PostAd
from django.contrib.auth import authenticate


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add your uap-mail address')

    class Meta:
        model = Account
        fields = ("email", "username", "first_name", "last_name", "reg_id", "department", "profile_pic", "cell_number", "password1", "password2")


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login info!")


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('username', 'profile_pic','cell_number')

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use.' % username)

    def clean_profile_pic(self):
        if self.is_valid():
            profile_pic = self.cleaned_data['profile_pic']
            return profile_pic

    def clean_cell_number(self):
        if self.is_valid():
            cell_number = self.cleaned_data['cell_number']
            return cell_number


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = PostAd
        fields = ['title', 'price', 'description', 'category', 'image1', 'image2']



