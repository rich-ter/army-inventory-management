from django import template

register = template.Library()

@register.inclusion_tag('filters/form.html', takes_context=True)
def render_filter_form(context, filter):
    return {'filter': filter}
