from django import forms 
from .models import Item



class ItemFrom(forms.ModelForm):
    class Meta:
        model = Item
        fields =['item_name','item_desc','item_prise','item_image']