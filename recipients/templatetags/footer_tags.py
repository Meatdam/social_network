from django import template

from recipients.forms import AddRecipientsForm

register = template.Library()


@register.inclusion_tag('recipients/recipients_form_tag.html')
def client_form():
    return {'client_form': AddRecipientsForm()}
