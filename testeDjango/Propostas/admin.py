from django.contrib import admin

from .models import CampoProposta, Proposta, ValorCampo


@admin.register(CampoProposta)
class CampoPropostaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo')
    

class ValorCampoInline(admin.TabularInline):
    model = ValorCampo
    extra = 1

class PropostaAdmin(admin.ModelAdmin):
    inlines = [ValorCampoInline]

admin.site.register(Proposta, PropostaAdmin)
