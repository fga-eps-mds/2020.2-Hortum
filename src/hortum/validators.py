from django.db import DataError

from rest_framework.utils.representation import smart_repr
from rest_framework.exceptions import ValidationError

# Implementação para retornar `False` em vez de uma exceção
def qs_exists(queryset):
    try:
        return queryset.exists()
    except (TypeError, ValueError, DataError):
        return False

# Implementação para retornar uma queryset vazia em vez de exceção
def qs_filter(queryset, **kwargs):
    try:
        return queryset.filter(**kwargs)
    except (TypeError, ValueError, DataError):
        return queryset.none()

class UniqueValidator:
    '''
    Validação que checa se um campo é único.
    Implementação baseada no `UniqueValidator` porém modificada
    para checagem do próprio valor
    '''
    message = 'Este campo deve ser único.'
    requires_context = True

    def __init__(self, queryset, message=None, lookup='exact'):
        self.queryset = queryset
        self.message = message or self.message
        self.lookup = lookup

    def filter_queryset(self, value, queryset, field_name):
        '''
        Queryset que filtra todos values iguais
        '''
        filter_kwargs = {'%s__%s' % (field_name, self.lookup): value}
        return qs_filter(queryset, **filter_kwargs)

    def __call__(self, value, serializer_field):
        # Determinando o nome do campo
        field_name = serializer_field.source_attrs[-1]

        queryset = self.queryset
        queryset = self.filter_queryset(value, queryset, field_name)
        if qs_exists(queryset):
            raise ValidationError(self.message, code='unique')

    def __repr__(self):
        return '<%s(queryset=%s)>' % (
            self.__class__.__name__,
            smart_repr(self.queryset)
        )

class ExistingValidator:
    '''
    Validação que checa se um campo é existe.
    Implementação baseada no `UniqueValidator`
    '''
    message = '{value} inexistente.'
    requires_context = True

    def __init__(self, queryset, lookup='exact'):
        self.queryset = queryset
        self.lookup = lookup

    def filter_queryset(self, value, queryset, field_name):
        '''
        Queryset que filtra todos values iguais
        '''
        filter_kwargs = {'%s__%s' % (field_name, self.lookup): value}
        return qs_filter(queryset, **filter_kwargs)

    def __call__(self, value, serializer_field):
        # Determinando o nome do campo
        field_name = '__'.join(serializer_field.source_attrs)

        # Montando a mensagem baseada no campo
        self.message = self.message.format(value=' '.join(serializer_field.source_attrs).capitalize())

        queryset = self.queryset
        queryset = self.filter_queryset(value, queryset, field_name)
        if not qs_exists(queryset):
            raise ValidationError(self.message, code='unique')

    def __repr__(self):
        return '<%s(queryset=%s)>' % (
            self.__class__.__name__,
            smart_repr(self.queryset)
        )

class PasswordValidator:
    '''
    Validação que checa se a senha passada está correta.
    Implementação baseada no `UniqueValidator`.
    '''
    message = 'Senha incorreta.'
    requires_context = True

    def __init__(self, password='password', message=None):
        self.password = password
        self.message = message or self.message

    def __call__(self, value, serializer):
        if not serializer.context['request'].user.check_password(value):
            raise ValidationError(self.message)

    def __repr__(self):
        return '<%s(password=%s)>' % (
            self.__class__.__name__,
            smart_repr(self.password)
        )