from django import forms 
from .models import Account  


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
        'class':"form-control"

    }))

    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':"Confirm Password",
        'class':"form-control"
    }))



    class Meta:
        model = Account
        fields = ['first_name','last_name','email','phone'] 

    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs) 

        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address' 
        self.fields['phone'].widget.attrs['placeholder'] = 'Enter Phone Number' 
        


        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    
    def clean(self):
        cleaned_data = super(RegistrationForm,self).clean()
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("repeat_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not Match"
            )
        
        

            






