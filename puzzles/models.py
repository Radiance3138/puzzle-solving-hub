from django.db import models
from .users import models

# TODO: After merging User branch, link ArgUserProfile model here
# TODO: Add any necessary imports for relationships
# TODO: figure out cipher method field (fk or choicefield?)

class PuzzleHub(models.Model):
    # Define fields for the PuzzleHub model
    title = models.CharField(max_length=200)
    description = models.TextField()
    source_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Relationships
    owner = models.ForeignKey(ArgUserProfile, on_delete=models.CASCADE, related_name='puzzles_owned')
    participants = models.ManyToManyField(ArgUserProfile, related_name='puzzles_participated')

    status = models.ChoiceField(choices = [
        ('active', 'Active'),
        ('solved', 'Solved'),
        ('archived', 'Archived'),
    ])

    def __str__(self):
        return self.title
    
class SourceTextEntry(models.Model):
    # Define fields for the SourceTextEntry model
    cipher_text = models.TextField()
    plain_text = models.TextField()
    method = models.CharField(max_length=100)
    key = models.CharFeild(max_length=100, blank=True, null=True)
    date_recorded = models.DateTimeField(auto_now_add=True)
    # Relationships
    puzzle_hub = models.ForeignKey(PuzzleHub, on_delete=models.CASCADE, related_name='related_arg')
    solver = models.ForeignKey(ArgUserProfile, on_delete=models.CASCADE, related_name='cipher_entries', blank=True, null=True)

    def __str__(self):
        return self.cipher_text
    