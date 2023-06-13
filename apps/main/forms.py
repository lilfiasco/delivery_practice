from django import forms
from .models import Food
from django.utils.text import slugify
import cyrtranslit
from PIL import Image
from django.core.exceptions import ValidationError as vale

class FoodForm(forms.ModelForm):
    
    class Meta:
        model = Food
        exclude = ('quantity',)

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        if commit:
            instance.save()  
            
        instance.slug = self.generate_slug() 
        instance.image = self.validate_image_size(instance)
        if commit:
            instance.save() 
        return instance

    def generate_slug(self):
        franchise = self.cleaned_data['franchise']
        category = self.cleaned_data['category']
        title = self.cleaned_data['title']
        slug = slugify(cyrtranslit.to_latin(f"{franchise.title}_{category.title}_{self.instance.title}", "ru"), allow_unicode=True)
        return slug

    def validate_image_size(self, instance):
        max_size = 2097152  # 2MB in bytes
        if instance.image.size > max_size:
            raise ValueError("The maximum file size allowed is 2MB.")
        width, height = Image.open(instance.image).size
        if width < 100 or height < 100:
            raise ValueError("The image dimensions should be at least 100x100 pixels.")
        return instance.image

