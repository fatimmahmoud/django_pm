from django import forms
from . import models
attrs = { 'class': 'form-control'}
#هذه هي الاستمارة الخاصة بإنشاء المشاريع، وتم تحديد أسماء حقولها ونوع كل حقل
class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category', 'title', 'description']
        widgets ={

            'category': forms.Select(attrs=attrs),
            'title': forms.TextInput(attrs=attrs), 
            'description': forms.Textarea(attrs=attrs),

        }

   
class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category', 'title', 'status']
        widgets ={

            'category': forms.Select(attrs=attrs),
            'title': forms.TextInput(attrs=attrs), 
            'status': forms.Select(attrs=attrs)

        }
