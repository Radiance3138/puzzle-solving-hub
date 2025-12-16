from django.db import models
from users.models import ArgUserProfile


# DONE: After merging User branch, link ArgUserProfile model here
# TODO: figure out cipher method field (fk or choicefield?)

class PuzzleHub(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    source_url = models.URLField(blank=True, null=True)

    owner = models.ForeignKey(ArgUserProfile, on_delete=models.CASCADE, related_name='puzzles_owned')
    participants = models.ManyToManyField(ArgUserProfile, related_name='puzzles_participated')

    status = models.CharField(
        max_length=10,
        choices = [
            ('active', 'Active'),
            ('solved', 'Solved'),
            ('archived', 'Archived'),
        ],
        default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class SourceTextEntry(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable=True)
    cipher_text = models.TextField()
    plain_text = models.TextField()
    method = models.CharField(max_length=100)
    key = models.CharField(max_length=100, blank=True, null=True)
    date_recorded = models.DateTimeField(auto_now_add=True)

    parent_entry = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='child_entries')
    puzzle_hub = models.ForeignKey(PuzzleHub, on_delete=models.CASCADE, related_name='related_arg')
    solver = models.ForeignKey(ArgUserProfile, on_delete=models.CASCADE, related_name='cipher_entries', blank=True, null=True)

    def __str__(self):
        return self.cipher_text
    