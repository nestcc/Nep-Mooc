from django import forms


class CreateCourse(forms.Form):
      cour_name = forms.CharField(required=True, max_length=20)
      cour_type = forms.IntegerField(required=True)
      cour_start = forms.DateTimeField(required=True)
      cour_end = forms.DateTimeField(required=True)
      cour_description = forms.TextInput()

