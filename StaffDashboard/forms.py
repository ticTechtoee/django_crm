from inquiry.models import Inquiry
from django.forms import ModelForm

class UpdateinquiryForm(ModelForm):
    class Meta:
        model = Inquiry
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(UpdateinquiryForm, self).__init__(*args, **kwargs)
       
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})