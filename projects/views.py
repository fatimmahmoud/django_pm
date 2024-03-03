from django.shortcuts import render
from django.views.generic import ListView, CreateView #نستخدم listview لعرض المشاريع
from django.urls import reverse_lazy
from . import models
from . import forms
# Create your views here.
class ProjectListView(ListView):
    model = models.Project
    template_name='project/list.html'

#نحن متفقين ان العروض هي حلقة الوصل بين المودلز والقوالب، لذا هنا ننشئ عرض
#يخبر المتصفح ماذا سيعرض 
class ProjectCreatView(CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'project/creat.html'
    success_url = reverse_lazy('project_List')



