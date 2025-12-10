from django.urls import path
from puzzles import views


urlpatterns = [
    path('entries/', views.SourceTextEntryListView.as_view(), name='source_text_entry_list'),
    path('entries/<int:pk>/', views.SourceTextEntryDetailView.as_view(), name='source_text_entry_detail'),
    path('entries/create/', views.SourceTextEntryCreateView.as_view(), name='source_text_entry_create'),
    path('entries/<int:pk>/update/', views.SourceTextEntryUpdateView.as_view(), name='source_text_entry_update'),
    path('entries/<int:pk>/delete/', views.SourceTextEntryDeleteView.as_view(), name='source_text_entry_delete'),
]
