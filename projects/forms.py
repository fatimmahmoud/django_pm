from django import forms
from . import models

#هذه هي الاستمارة الخاصة بإنشاء المشاريع، وتم تحديد أسماء حقولها ونوع كل حقل
class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category', 'title', 'description']
        widgets ={

            'category': forms.Select(),
            'title': forms.TextInput(), 
            'descriptoin': forms.Textarea()

        }

   
class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category', 'title', 'status']
        widgets ={

            'category': forms.Select(),
            'title': forms.TextInput(), 
            'status': forms.Select()

        }
