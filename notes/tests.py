from django.test import TestCase
from .models import Note
from django.core.exceptions import ValidationError

class NoteModelTest(TestCase):

    def test_notes_can_be_created(self):
        note = Note.objects.create(
            title="Test Note",
            description="This is valid description"
        )
        self.assertEqual(note.title, "Test Note")

    def test_error_occurs_if_description_is_less_than_10_chars_long(self):
        note = Note(
            title="Short",
            description="short"
        )
        with self.assertRaises(ValidationError):
            note.full_clean()