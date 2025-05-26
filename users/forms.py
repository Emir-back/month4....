from django import forms 
from . import models
from django.contrib.auth.forms import UserCreationForm

GENDER = (
    ('male','male'),
    ('female' , 'female'),

)

class CustomRegisterForm(UserCreationForm):
    phone_number = forms.CharField(max_length=12, required=True,label='Укажите номер телефона')
    age = forms.IntegerField(required=True,label='Укажите возраст')
    email = forms.EmailField(required=True, label='Укажите почту')
    gender = forms.ChoiceField(choices=GENDER, required=True)

    class Meta:
        model = models.CustomUser,
        fields = ('username', 'phone_number', 'age', 'email', 'gender','password1','password2','first_name','last_name' )
        def save(self, commit=True):
            user = super().save(commit=False)
            user.phone_number = self.cleaned_data['phone_number']
            user.age = self.cleaned_data['age']
            user.email = self.cleaned_data['email']
            user.gender = self.cleaned_data['gender']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            if commit:
                user.save()
            return user
         