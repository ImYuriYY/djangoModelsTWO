from django import forms


class CreatePost(forms.Form):
    title = forms.CharField(label='Заголовок',
        widget=forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder':'Это моя новость'
    }))
    content = forms.CharField(label='Контент',
        widget=forms.Textarea(attrs={
        'class': 'form-textarea'
    }))
    urladdress = forms.CharField(label='URL', required=False,
        widget=forms.TextInput(attrs={
        'class': 'form-input'
    }))
    isPublic = forms.ChoiceField(label='Публикация', required=False,
        widget=forms.CheckboxInput(attrs={
        'class': 'form-checkbox'
    }))

    category = forms.ChoiceField(label='Категория', required=False,
        widget=forms.Select(attrs={
        'class': 'form-input'
        }),
        choices=(
            (1, 'Категория не выбрана'), (2, 'Категория 1'), (3, 'Категория 2')
        ),
    )