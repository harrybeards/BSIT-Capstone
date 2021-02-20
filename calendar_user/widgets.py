from django.forms import DateInput, TimeInput, DateTimeInput


class BootstrapDateTimePickerInput(DateTimeInput):
    template_name = 'widgets/bootstrap_datetimepicker.html'

    def get_context(self, name, value, attrs):
        datetimepicker_id = 'datetimepicker_{name}'.format(name=name)
        if attrs is None:
            attrs = dict()
        attrs['data-target'] = '#{id}'.format(id=datetimepicker_id)
        attrs['class'] = 'form-control datetimepicker-input'
        context = super().get_context(name, value, attrs)
        context['widget']['datetimepicker_id'] = datetimepicker_id

        return context


class FengyuanChenDatePickerInput(DateInput):
    template_name = 'widgets/fengyuanchen_datepicker.html'


class WickedPicker(TimeInput):
    template_name = 'widgets/wickedpicker.html'