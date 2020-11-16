from django import forms


class CarForm(forms.Form):
    manufacturer = forms.CharField(max_length=20, required=False)
    model = forms.CharField(max_length=10, required=False)
    year = forms.IntegerField(required=False)
    transmission = forms.MultipleChoiceField(choices=[(1, 'manual'), (2, 'automatic'), (3, 'robot')], required=False)
    color = forms.CharField(max_length=10, required=False)

