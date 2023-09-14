from django import forms


class UpdateItemForms(forms.Form):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'col': 5, 'rows': 5}),
        label='Описание:'
    )
    price = forms.IntegerField(label='Цена:')
