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

# Implementação que filtra dependendo do nome do campo
def filter_queryset(value, queryset, field_name, lookup):
    filter_kwargs = {'%s__%s' % (field_name, lookup): value}
    return qs_filter(queryset, **filter_kwargs)

class UniqueValidator:
    '''
    Validação que checa se um campo é único.
    Implementação baseada no `UniqueValidator` porém modificada
    para checagem do próprio valor
    '''
    message = 'Este campo deve ser único.'
    requires_context = True

    def __init__(self, queryset=None, message=None, lookup='exact'):
        self.queryset = queryset
        self.message = message or self.message
        self.lookup = lookup

    def __call__(self, value, serializer_field):
        # Determinando o nome do campo
        field_name = '__'.join(serializer_field.source_attrs)

        # Filtragem da queryset
        queryset = self.queryset or serializer_field.context['view'].get_queryset()
        queryset = filter_queryset(value, queryset, field_name, self.lookup)
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

    def __init__(self, queryset=None, lookup='exact'):
        self.queryset = queryset
        self.lookup = lookup

    def __call__(self, value, serializer_field):
        # Determinando o nome do campo
        field_name = '__'.join(serializer_field.source_attrs)

        # Montando a mensagem baseada no campo
        self.message = self.message.format(value=serializer_field.source_attrs[-1].capitalize())

        # Filtragem da queryset
        queryset = self.queryset or serializer_field.context['view'].get_queryset()
        queryset = filter_queryset(value, queryset, field_name, self.lookup)
        if not qs_exists(queryset):
            raise ValidationError(self.message, code='unique')

    def __repr__(self):
        return '<%s(queryset=%s)>' % (
            self.__class__.__name__,
            smart_repr(self.queryset)
        )