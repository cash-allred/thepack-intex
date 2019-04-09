from django import forms

from base.utils import generate_bootstrap_widgets_for_all_fields

from . import (
    models
)


class OverdoseDeaths(forms.ModelForm):
    class Meta:
        model = models.OverdoseDeaths
        fields = '__all__'
        widgets = generate_bootstrap_widgets_for_all_fields(models.OverdoseDeaths)

class Prescription(forms.ModelForm):
    class Meta:
        model = models.Prescription
        fields = '__all__'
        widgets = generate_bootstrap_widgets_for_all_fields(models.Prescription)

class Drug(forms.ModelForm):
    class Meta:
        model = models.Drug
        fields = '__all__'
        widgets = generate_bootstrap_widgets_for_all_fields(models.Drug)

class Doctor(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = '__all__'
        widgets = generate_bootstrap_widgets_for_all_fields(models.Doctor)

