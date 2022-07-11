from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from .models import Tags, Task


def complete_button(request, pk):

    task = Task.objects.get(pk=pk)
    task.status = not task.status
    task.save()

    return HttpResponseRedirect(reverse(f"homepage"))


class TagsListView(generic.ListView):
    model = Tags
    context_object_name = "tags"
    template_name = "to_do_list/tags_list.html"


class TagsCreateView(generic.CreateView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("tags")
    template_name = "to_do_list/tags_form.html"


class TagsUpdateView(generic.UpdateView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("tags")
    template_name = "to_do_list/tags_form.html"


class TagsDeleteView(generic.DeleteView):
    model = Tags
    success_url = reverse_lazy("tags")
    template_name = "to_do_list/tags_delete.html"


class ToDoListView(generic.ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "to_do_list/tasks_list.html"


class ToDoCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("homepage")
    template_name = "to_do_list/tasks_form.html"


class ToDoUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("homepage")
    template_name = "to_do_list/tasks_form.html"


class ToDoDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("homepage")
    template_name = "to_do_list/tasks_delete.html"
