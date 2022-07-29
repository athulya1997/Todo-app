from django.forms import ModelForm
from app1.models import *

class TodoForm(ModelForm): 
    class Meta:
        model = Todo
        fields = ['title','status','priority']