from app1.models import Portfolio
from django.forms import ModelForm,ValidationError
class ContactForm(ModelForm):
    class Meta:
        model= Portfolio
        fields= '__all__'

def clean_first_name(self):
    data = self.cleaned_data["first_name"]
    if len(data):
        raise ValidationError('name_error')
    else:
        return data
