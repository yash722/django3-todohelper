from django.forms import ModelForm
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo #Specifying where to get the form
        fields = ['title', 'memo', 'important'] #Fields in the form
