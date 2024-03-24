from django import forms

class PresentationUploadForm(forms.Form):
    presentation = forms.FileField(label='Upload Presentation')