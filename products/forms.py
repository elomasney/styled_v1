from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductFeature


class ProductForm(forms.ModelForm):
    """ Creates instance of Product Form """
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('online_price',)

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductFeatureForm(forms.ModelForm):
    """ Creates instance of Product Feature Form """
    class Meta:
        model = ProductFeature
        fields = '__all__'
        widgets = {
            'product': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
