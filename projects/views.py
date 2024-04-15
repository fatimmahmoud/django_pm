from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView #نستخدم listview لعرض المشاريع
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import models
from . import forms
# Create your views here.
class ProjectListView(LoginRequiredMixin, ListView):
    model = models.Project
    template_name='project/list.html'
    paginate_by = 3

    def get_queryset(self):
        query_set = super().get_queryset()
        where = {}
        q = self.request.GET.get('q', None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)

#نحن متفقين ان العروض هي حلقة الوصل بين المودلز والقوالب، لذا هنا ننشئ عرض
#يخبر المتصفح ماذا سيعرض 

class ProjectCreatView(LoginRequiredMixin, CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'project/creat.html'
    success_url = reverse_lazy('project_List')



class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = 'project/Update.html'
    
    def get_success_url(self) -> str:
        return reverse('project_update', args=[self.object.id])



class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Project
    template_name = 'project/delete.html'

    success_url = reverse_lazy('project_List')




class TaskCreatView(LoginRequiredMixin, CreateView):
    model = models.Task
    fields= ['project', 'description']
    http_method_names = ['post']
    def get_success_url(self) -> str:
        return reverse('project_update', args=[self.object.project.id])
    


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Task
    fields= ['is_completed']
    http_method_names = ['post']

    def get_success_url(self) -> str:
        return reverse('project_update', args=[self.object.project.id])

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Task

    def get_success_url(self) -> str:
        return reverse('project_update', args=[self.object.project.id])