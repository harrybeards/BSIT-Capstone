from django.forms import DateInput, TimeInput


class FengyuanChenDatePickerInput(DateInput):
    template_name = 'fengyuanchen_datepicker.html'


class WickedPicker(TimeInput):
    template_name = 'wickedpicker.html'