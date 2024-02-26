from django import template

register = template.Library()

@register.filter
def get_total_for_proion(totals, proion_id):
    return totals.get(proion_id, 0)
