from django.forms import ModelForm
from puzzles.models import SourceTextEntry

class SourceTextEntryForm(ModelForm):
    class Meta:
        model = SourceTextEntry
        fields = ['cipher_text', 'plain_text', 'method', 'key', 'solver', 'parent_entry', 'puzzle_hub']
        labels = {
            'cipher_text': 'Cipher Text',
            'plain_text': 'Plain Text',
            'method': 'Method',
            'key': 'Key',
            'solver': 'Solver',
            'parent_entry': 'Parent Entry',
            'puzzle_hub': 'Puzzle Hub',
        }
        help_texts = {
            'cipher_text': 'Enter the encrypted text here.',
            'plain_text': 'The decrypted text will be displayed here.',
            'method': 'Specify the method used for encryption/decryption.',
            'key': 'Provide the key used in the process.',
            'solver': 'Select the solver associated with this entry.',
            'parent_entry': 'Link to a parent source text entry if applicable.',
            'puzzle_hub': 'Associate this entry with a specific puzzle hub.',
        }
