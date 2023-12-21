from django import forms
from .models import UserProfile, District, Branch


class DistrictForm(forms.ModelForm):

    class Meta:
        model = District
        fields = ['name']


class BranchForm(forms.ModelForm):

    class Meta:
        model = Branch
        fields = ['name', 'district']


class UserDetails(forms.ModelForm):
    genders = (('ML', 'Male'), ('FL', 'Female'), ('TR', 'Transgender'))
    gender = forms.ChoiceField(choices=genders, widget=forms.RadioSelect)

    account_types = (('SV', 'Savings account'), ('CR', 'Current account'))
    account_type = forms.ChoiceField(choices=account_types)

    materialss = (('CRD', 'Credit Card'), ('DBD', 'Debit Card'), ('CQB', 'Cheque Book'), ('PSB', 'Passbook'))
    materials = forms.ChoiceField(choices=materialss, widget=forms.RadioSelect)

    dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form', 'type': 'date'}))

    class Meta:
        model = UserProfile
        fields = ['name', 'dob', 'age', 'gender', 'phone', 'address', 'district', 'branch', 'account_type', 'materials']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass
