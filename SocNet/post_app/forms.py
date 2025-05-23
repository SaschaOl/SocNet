from django import forms
from .models import Post

class MultipleImageInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleImageField(forms.ImageField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleImageInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result

class PostForm(forms.ModelForm):
    images = MultipleImageField()

    class Meta:
        model = Post
        fields = ['title', 'tags', 'post_text']


class PostDeletionForm(forms.Form):
    post_id = forms.IntegerField(min_value= 0, widget= forms.NumberInput(attrs= {'id': 'deleteIDInput','hidden': '1'}))