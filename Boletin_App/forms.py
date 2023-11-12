
from django import forms
from django.core.exceptions import ValidationError
import re

class TuFormulario(forms.Form):
    fecha_inicio = forms.DateField()
    fecha_fin = forms.DateField()
    dias_semana = forms.MultipleChoiceField(
        choices=[('lunes', 'Lunes'), ('martes', 'Martes'), ('miercoles', 'Miércoles'),
                 ('jueves', 'Jueves'), ('viernes', 'Viernes'), ('sabado', 'Sábado'), ('domingo', 'Domingo')],
        widget=forms.CheckboxSelectMultiple,
    )
    correo_electronico = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get("fecha_inicio")
        fecha_fin = cleaned_data.get("fecha_fin")
        dias_semana = cleaned_data.get("dias_semana")
        correo_electronico = cleaned_data.get("correo_electronico")

        # Validación: fecha de fin debe ser igual o superior a la fecha de inicio
        if fecha_inicio and fecha_fin and fecha_fin < fecha_inicio:
            raise ValidationError("La fecha de fin debe ser igual o posterior a la fecha de inicio.")

        # Validación: al menos un día de la semana seleccionado
        if not dias_semana:
            raise ValidationError("Selecciona al menos un día de la semana.")

        # Validación: no más de 3 días de la semana seleccionados
        if dias_semana and len(dias_semana) > 3:
            raise ValidationError("Selecciona como máximo 3 días de la semana.")

        # Validación: el correo electrónico debe pertenecer a la organización iesmartinezm.es
        if not re.match(r".*@iesmartinezm\.es$", correo_electronico):
            raise ValidationError("El correo electrónico debe pertenecer a la organización iesmartinezm.es.")