from django import  forms
from .models import  user

class studentregistration(forms.ModelForm):
    class Meta:
        # user is the model table name
        model=user
        fields=['name','email','password','gender','birth_date']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
                # render_value=True  ------ > karne se password value show hogi
            'password':forms.PasswordInput(render_value=True,
                                           attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'forms-control'}),
            'birth_date':forms.DateTimeInput(attrs={'class':'form-control'}),
        }