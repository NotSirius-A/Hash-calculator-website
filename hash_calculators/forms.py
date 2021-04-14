from django import forms


class HashInputForm(forms.Form):
    widget = forms.TextInput(attrs={
                                'placeholder': 'Write some text here!',
                                'size': 100
                                }
                            )

    text = forms.CharField(label='Type a message you want to hash below!', max_length=100, required=False ,widget=widget)

    def clean(self):
        pass