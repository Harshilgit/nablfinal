from django import forms
from calibration_management_app.models import *




class DateInput(forms.DateInput):
    input_type = 'date'


class AddNewJobForm(forms.ModelForm):
    class Meta():
        model = AddNewJob
        fields = '__all__'
        widgets = {
        'inward_date': DateInput(),
        }

class PartyForm(forms.ModelForm):
    class Meta():
        model = Party
        fields = '__all__'


class InstrumentInfoForm(forms.ModelForm):
    class Meta():
        model = InstrumentInfo
        fields = '__all__'


class MakeForm(forms.ModelForm):
    class Meta():
        model = Make
        fields = '__all__'


class ModelForm(forms.ModelForm):
    class Meta():
        model = Model
        fields = '__all__'


class UUCForm(forms.ModelForm):
    class Meta():
        model = UUC
        fields = '__all__'


class TodoForm(forms.ModelForm):
    class Meta():
        model = Todo
        fields = '__all__'
        widgets = {
        'deadline': DateInput(),
        }


class MasterInstrumentForm(forms.ModelForm):
    class Meta():
        model = MasterInstrument
        fields = '__all__'
        widgets = {
        'inservice_date': DateInput(),
        'purchase_date': DateInput(),
        'date_of_receipt': DateInput(),
        'date_of_inspection': DateInput(),
        'issue_date': DateInput(),
        'exp_date': DateInput(),
        }


class FinalcertForm(forms.ModelForm):
    class Meta():
        model = Finalcert
        fields = '__all__'


class CertInfoForm(forms.ModelForm):
    class Meta():
        model = Certificate_info
        fields = '__all__'
        widgets = {
        'cal_date': DateInput(),
        'due_date': DateInput(),
        }

class PressureForm(forms.ModelForm):
    class Meta():
        model = Certificate_info
        fields = '__all__'
