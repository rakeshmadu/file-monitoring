from django import forms
from .models import Register,Fir_Details,Display

class RegForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
        widgets = {'password':forms.PasswordInput}
        exclude = ('reg_id',)

class Loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class FirForm(forms.ModelForm):
    class Meta:
        model = Fir_Details
        fields = '__all__'
        exclude = ('fir_number',)

class Displayform(forms.ModelForm):
    class Meta:
        model = Display
        fields = '__all__'
