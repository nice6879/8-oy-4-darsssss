from django import forms
from Goods.models import Info

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'phone': forms.TextInput(attrs={'type': 'tel'}),  
        }

    def clean_phone(self):
        """Custom validation for phone number (optional)"""
        phone = self.cleaned_data['phone']

        return phone
