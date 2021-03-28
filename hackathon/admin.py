from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    model = CustomUsuario
    list_display = ('first_name', 'last_name', 'email', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name',)}),
        ('Permissões', {'fields': ('is_active', 'is_staff',
                                   'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'banner', 'iframe_url')


@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    list_display = ('estado', 'nome', 'descricao',
                    'bio', 'banner', 'iframe_url')


@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('lugar', 'nome', 'descricao',
                    'banner', 'iframe_url')


@admin.register(Hospedagem)
class HospedagemAdmin(admin.ModelAdmin):
    list_display = ('lugar', 'nome', 'descricao',
                    'banner', 'iframe_url')


@admin.register(Restaurante)
class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('lugar', 'nome', 'descricao',
                    'banner', 'iframe_url')


@admin.register(Viagem)
class ViagemAdmin(admin.ModelAdmin):
    list_display = ('salario', 'porcentagem', 'estado')


@admin.register(Extras)
class ExtrasAdmin(admin.ModelAdmin):
    list_display = ('viagem',)
