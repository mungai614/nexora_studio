# forms.py
from django import forms
from .models import Testimonial

from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['client_name', 'company', 'client_image', 'message', 'rating']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'message': forms.Textarea(attrs={'rows':4}),
        }

def clean_client_image(self):
    image = self.cleaned_data.get('client_image')
    if image:
        if image.size > 2*1024*1024:  # 2MB limit
            raise forms.ValidationError("Image too large. Max 2MB.")
        if not image.content_type in ['image/jpeg', 'image/png']:
            raise forms.ValidationError("Only JPEG or PNG allowed.")
    return image
