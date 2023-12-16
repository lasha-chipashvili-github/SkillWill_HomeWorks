from .models import CustomUser
from django import forms

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
       # fields = UserCreationForm.Meta.fields + ('date_of_birth',)
        fields = ["username", "email", "password", "date_of_birth"]

        labels = {
            "user_name": "*Username",
            "password": "*Password",
            "date_of_birth": "*Birth Date"
        }
        widgets = {
            "user_name":  forms.TextInput(attrs={'placeholder':'ex:test','autocomplete': 'off'}),
            "password": forms.PasswordInput(attrs={'placeholder':'********','autocomplete': 'off','data-toggle': 'password'}),
            "date_of_birth": forms.DateInput(format=('%Y-%m-%d'),
        attrs={'class': 'form-control',
               'placeholder': 'Select a date',
               'type': 'date'
              })
        }



#%% hypothetic code

# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#
# class CustomUserCreationForm(UserCreationForm):
#
#     class Meta:
#         model = CustomUser
#         fields = ("email", "passwrod", "date_of_birth")
# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = fields = ("email", "passwrod", "date_of_birth")

