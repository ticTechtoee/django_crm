from .models import Inquiry
from django.forms import ModelForm

class inquiryForm(ModelForm):
    class Meta:
        model = Inquiry
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(inquiryForm, self).__init__(*args, **kwargs)
       
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})