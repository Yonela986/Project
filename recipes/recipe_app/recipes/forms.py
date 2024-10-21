from django import forms
from django.contrib.auth.models import User
import random
import string

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['username', 'email']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.generate_random_password()  # Generate password
        user.set_password(password)  # Hash the password
        if commit:
            user.save()
        return user

    def generate_random_password(self, length=8):
        """Generate a random password."""
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))