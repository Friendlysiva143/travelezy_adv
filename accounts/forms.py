from django import forms
from .models import Account
class RegistrationForms(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter password'
    }))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm password'
    }))
    class Meta:
        model = Account
        fields=['first_name','last_name','email','phone_number','password']
    def __init__(self,*args,**kwargs):
        super(RegistrationForms,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder']="Enter First Name"
        self.fields['last_name'].widget.attrs['placeholder']="Enter Last Name"
        self.fields['email'].widget.attrs['placeholder']=" Enter Email"
        self.fields['phone_number'].widget.attrs['placeholder']="Enter Phone Number"
    def clean(self):
        cleaned_data=super(RegistrationForms,self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')
        if password!=confirm_password:
            raise forms.ValidationError(
                "password not matching"
            )