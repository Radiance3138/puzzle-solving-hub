from django.forms import ModelForm
from puzzles.models import SourceTextEntry

class SourceTextEntryForm(ModelForm):
    class Meta:
        model = SourceTextEntry
        fields = ['cipher_text', 'plain_text', 'method', 'key']
        labels = {
            'cipher_text': 'Cipher Text',
            'plain_text': 'Plain Text',
            'method': 'Method',
            'key': 'Key',
        }
        help_texts = {
            'cipher_text': 'Enter the encrypted text here.',
            'plain_text': 'The decrypted text will be displayed here.',
            'method': 'Specify the method used for encryption/decryption.',
            'key': 'Provide the key used in the process.',
        }
