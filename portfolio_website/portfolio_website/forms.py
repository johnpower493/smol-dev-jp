from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, max_length=500)

class PortfolioForm(forms.Form):
    project_name = forms.CharField(max_length=200)
    project_description = forms.CharField(widget=forms.Textarea, max_length=1000)
    project_url = forms.URLField()
    project_image = forms.ImageField()