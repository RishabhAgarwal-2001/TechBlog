from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class AuthorForm(forms.Form):
    CATEGORY_CHOICES = [("S", "Science"), ("E", "Engineering"), ("T", "Technology")]
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Title'}))
    content = forms.CharField(widget=CKEditorUploadingWidget())
    category = forms.ChoiceField(choices = CATEGORY_CHOICES)
