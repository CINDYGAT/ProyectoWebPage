from django.contrib.auth.forms import SetPasswordForm
from django.utils.translation import gettext_lazy as _
from django import forms  # Importar forms para usar ValidationError

class CustomSetPasswordForm(SetPasswordForm):
    error_messages = {
        'password_mismatch': _("Las contraseñas no coinciden."),
        'password_too_similar': _("La contraseña no puede ser demasiado similar a su información personal."),
        'password_too_short': _("La contraseña debe tener al menos 12 caracteres."),
        'password_too_common': _("La contraseña es demasiado común."),
        'password_entirely_numeric': _("La contraseña no puede ser solo numérica."),
    }

    # Validar requisitos personalizados (mayúscula, número, símbolo)
    def clean_new_password1(self):
        password = self.cleaned_data.get('new_password1')
        
        # Validar mayúscula
        if not any(c.isupper() for c in password):
            raise forms.ValidationError(
                _("La contraseña debe contener al menos una letra mayúscula.")
            )

        # Validar número
        if not any(c.isdigit() for c in password):
            raise forms.ValidationError(
                _("La contraseña debe contener al menos un número.")
            )

        # Validar símbolo especial
        special_chars = ['*', '#', '@', '$', '&', '!', '?', '%']
        if not any(c in special_chars for c in password):
            raise forms.ValidationError(
                _("La contraseña debe contener al menos un símbolo especial (*, #, @, $, &, !, ?, %).")
            )

        return password

