from django import forms
from app.models import Technology

class JobChangeListForm(forms.ModelForm):
    # here we only need to define the field we want to be editable
    technology = forms.ModelMultipleChoiceField(
        queryset=Technology.objects.all(), required=False)