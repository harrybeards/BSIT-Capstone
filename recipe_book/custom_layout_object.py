# We have to create CollectionForm with our formset to be rendered as fields
# inside of it. This is not straightforward because crispy-forms doesn’t have
# a layout object for a formset like it has it for a Div or HTML.
# The best solution is to create a custom crispy Layout Object.
from crispy_forms.layout import LayoutObject, TEMPLATE_PACK
from django.shortcuts import render
from django.template.loader import render_to_string


class Formset(LayoutObject):
    template = 'recipe_book/formset.html'

    def __init__(self, formset_name_in_context, template=None):
        self.formset_name_in_context = formset_name_in_context
        self.fields = []
        if template:
            self.template = template

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        formset = context[self.formset_name_in_context]
        return render_to_string(self.template, {'formset': formset})
