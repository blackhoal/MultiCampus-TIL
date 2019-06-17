from django import forms

class BoardForm(forms.Form):
    title = forms.CharField(
        max_length=10,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'title',
                'placeholder': 'Enter the title'
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'content-type',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        )
    )