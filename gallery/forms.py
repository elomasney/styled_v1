from django import forms
from products.widgets import CustomClearableFileInput
from .models import Image, Collection


class GalleryForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = '__all__'
        exclude = ('upvote',)

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        collections = Collection.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in collections]

        self.fields['collection'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
