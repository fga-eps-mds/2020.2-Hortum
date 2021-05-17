from rest_framework.exceptions import ValidationError

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