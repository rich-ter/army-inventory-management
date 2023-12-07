from django.contrib import admin 
from .models import Proion, Paragelia, Paraliptis, Apothema, Apothiki, PliroforiesParagellias 
from django.forms import inlineformset_factory

# Register your models here
# admin.site.register(Proion)
admin.site.register(Paraliptis)



class ApothemaInline(admin.TabularInline):  # or admin.StackedInline
    model = Apothema
    extra = 1  # Number of empty forms to display

class ProionAdmin(admin.ModelAdmin):
    inlines = [ApothemaInline]


class PliroforiesParagelliasInline(admin.TabularInline):  # or admin.StackedInline
    model = PliroforiesParagellias
    extra = 1  # Number of empty forms to display

class ParageliaAdmin(admin.ModelAdmin):
    inlines = [PliroforiesParagelliasInline]

admin.site.register(Paragelia, ParageliaAdmin)

admin.site.register(Proion, ProionAdmin)
