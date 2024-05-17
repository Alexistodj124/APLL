from django import forms
from .models import Empleados

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ['EmpleadoDPI', 'Nombres', 'Apellidos', 'Sueldo']

class UserForm(forms.ModelForm):
    class Meta:
        model=Empleados
        fields =('EmpleadoDPI', 'Nombres', 'Apellidos', 'Sueldo')
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
