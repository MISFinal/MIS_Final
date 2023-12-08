from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    dob = forms.DateField(help_text="Required. Format: YYYY-MM-DD")
    phone_number = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'dob', 'phone_number', 'address')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_profile = UserProfile.objects.create(
                user=user,
                dob=self.cleaned_data['dob'],
                phone_number=self.cleaned_data['phone_number'],
                address=self.cleaned_data['address']
            )
        return user
