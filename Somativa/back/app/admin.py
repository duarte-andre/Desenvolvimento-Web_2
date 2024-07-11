from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class AdminUsuarioCustomizado(UserAdmin):
    model = UsuarioCustomizado
    list_display = ['id', 'email', 'cpf']
    list_display_links = ('id', 'email', 'cpf',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions',)}),
        ('Management', {'fields': ('last_login',)}),
        ('Custom fields', {'fields': ('cpf', 'telefone', 'endereco',)}),
    )
    filter_horizontal = ('groups', 'user_permissions',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'groups', 'user_permissions',)
        }),
    )    
    search_fields = ['email',]
    ordering = ['email']

admin.site.register(UsuarioCustomizado, AdminUsuarioCustomizado)

class AdminCategoria(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Categoria, AdminCategoria)

class AdminLivro(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'foto_capa', 'categoria', ]
    list_display_links = ('id', 'titulo', 'foto_capa', 'categoria', )
    search_fields = ('titulo',)
    list_per_page = 10

admin.site.register(Livro, AdminLivro)

class AdminEmprestimo(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'status', 'data_realizacao', 'data_devolucao','quantidade', 'livro']
    list_display_links = ('id', 'usuario', 'status', 'data_realizacao', 'data_devolucao','quantidade', 'livro',)
    search_fields = ('usuario__email',)
    list_per_page = 10

admin.site.register(Emprestimo, AdminEmprestimo)


