from django import forms

class New_Article(forms.Form):
    article_title = forms.CharField(max_length=20)
    article_annotation = forms.CharField(max_length=200)
    article_preview_image = forms.ImageField()
    article_text = forms.CharField(widget=forms.TextInput)
    article_pictures = forms.ImageField()