from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from puzzles.models import SourceTextEntry
from puzzles.forms import SourceTextEntryForm


class SourceTextEntryListView(ListView):
    model = SourceTextEntry
    template_name = 'puzzle/source_text_entry_list.html'
    context_object_name = 'entries'

class SourceTextEntryDetailView(DetailView):
    model = SourceTextEntry
    template_name = 'puzzle/source_text_entry_detail.html'
    context_object_name = 'entry'
    
class SourceTextEntryCreateView(CreateView):
    model = SourceTextEntry
    template_name = 'puzzle/source_text_entry.html'
    form_class = SourceTextEntryForm
    success_url = reverse_lazy('source_text_entry_list')

    def form_valid(self, form):
        related_puzzle_hub_id = self.request.GET.get('puzzle_hub_id')
        related_parent_entry_id = self.request.GET.get('parent_entry_id')
        related_solver_id = self.request.GET.get('solver_id')

        form.instance.puzzle_hub_id = related_puzzle_hub_id
        form.instance.parent_entry_id = related_parent_entry_id
        form.instance.solver_id = related_solver_id
        
        return super().form_valid(form)

                
class SourceTextEntryUpdateView(UpdateView):
    model = SourceTextEntry
    template_name = 'puzzle/source_text_entry_update.html'
    form_class = SourceTextEntryForm
    success_url = reverse_lazy('source_text_entry_list')
    
    def form_valid(self, form):
        related_puzzle_hub_id = self.request.GET.get('puzzle_hub_id')
        related_parent_entry_id = self.request.GET.get('parent_entry_id')
        related_solver_id = self.request.GET.get('solver_id')

        form.instance.puzzle_hub_id = related_puzzle_hub_id
        form.instance.parent_entry_id = related_parent_entry_id
        form.instance.solver_id = related_solver_id
        
        return super().form_valid(form)

class SourceTextEntryDeleteView(DeleteView):
    model = SourceTextEntry
    template_name = 'puzzle/source_text_entry_delete.html'
    success_url = reverse_lazy('source_text_entry_list')
