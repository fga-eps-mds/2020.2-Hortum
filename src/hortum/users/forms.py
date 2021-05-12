from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import password_validation
from django import forms


class CustomPasswordForm(SetPasswordForm):
    """
    Form para redefinição de senha
    """
    error_messages = {
        'password_mismatch': ("As senhas inseridas não são iguais"),
    }
    new_password1 = forms.CharField(
        label=("Nova senha"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )

    new_password2 = forms.CharField(
        label=("Confirme nova senha"),
        widget=forms.PasswordInput,
        strip=False,
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password2

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user