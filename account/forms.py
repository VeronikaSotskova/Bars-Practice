from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.db.models import Q

from account.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    position = forms.ChoiceField(required=True, choices=CustomUser.POSITION_CHOICES)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'position')


class CustomUserChangeForm(UserChangeForm):
    position = forms.ChoiceField(required=True, choices=CustomUser.POSITION_CHOICES)

    class Meta:
        model = CustomUser
        fields = ('position',)


class UserRegistrationForm(forms.ModelForm):
    position = forms.ChoiceField(required=True, choices=CustomUser.POSITION_CHOICES)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'password', 'password2', 'position')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RoomForm(forms.Form):
    title = forms.CharField()
    staff = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.filter((~Q(position=CustomUser.MANAGER)) & Q(room=None) & (~Q(position=None))))

    def clean(self):
        raise forms.ValidationError('Something went wrong')


class AddStaffToRoom(forms.Form):
    staff = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.filter((~Q(position=CustomUser.MANAGER)) & Q(room=None) & (~Q(position=None))))
