from django import forms  



def check_form_m(value):
    if value.lower()[0] == 'm':
        raise forms.ValidationError('started with m')
    

def check_age(value):
    if value < 18:
        raise forms.ValidationError('age is less')
    
        

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, validators=[check_form_m])
    email = forms.EmailField()
    age = forms.IntegerField(validators=[check_age])
    message = forms.CharField(widget=forms.Textarea)
    reemail = forms.EmailField()
    botcatcher = forms.CharField(widget= forms.HiddenInput, required=False)
    
    
    def clean_botcatcher(self):
        a = self.cleaned_data['botcatcher']
        if len(a)>0:
            raise forms.ValidationError('age is less')
        return a
    
    def clean(self):
        e = self.cleaned_data['email']
        re = self.cleaned_data['reemail']
        if e != re:
            raise forms.ValidationError('its not matching')
