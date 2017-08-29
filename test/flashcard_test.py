import unittest
from uuid import uuid4, UUID
from mathsmaps.flashcard import Flashcard

class TestFlashcard(unittest.TestCase):
    def test_make_flashcard(self):
        new_flashcard = Flashcard(title="My Flashcard"
                                  ,text="This is a flashcard."
                                  )
        self.assertEqual(new_flashcard.title, "My Flashcard")
        self.assertEqual(new_flashcard.text, "This is a flashcard.")
    
    def test_make_flashcard_title_default(self):
        new_flashcard = Flashcard(text="This is a flashcard.")
        self.assertEqual(new_flashcard.title, "Untitled")
        self.assertEqual(new_flashcard.text, "This is a flashcard.")
    
    def test_make_flashcard_text_default(self):
        new_flashcard = Flashcard(title="My Flashcard")
        self.assertEqual(new_flashcard.title, "My Flashcard")
        self.assertEqual(new_flashcard.text, "")

    def test_make_flashcard_both_default(self):
        new_flashcard = Flashcard()
        self.assertEqual(new_flashcard.title, "Untitled")
        self.assertEqual(new_flashcard.text, "")
    
    def test_make_flashcard_from_dictionary(self):
        new_flashcard = Flashcard(**{"title":"My Flashcard"
                            ,"text":"This is a flashcard."
                            })
        self.assertEqual(new_flashcard.title, "My Flashcard")
        self.assertEqual(new_flashcard.text, "This is a flashcard.")
    
    def test_make_flashcard_ignoring_extra_arguments(self):
        new_flashcard = Flashcard(**{"title":"My Flashcard"
                                  ,"text":"This is a flashcard."
                                  ,"random_unused_argument": "DON'T USE THIS"
                                  })
        self.assertEqual(new_flashcard.title, "My Flashcard")
        self.assertEqual(new_flashcard.text, "This is a flashcard.")
        with self.assertRaises(AttributeError):
            new_flashcard.random_unused_argument
    
    def test_default_uuid(self):
        new_flashcard = Flashcard()
        self.assertIsInstance(new_flashcard.id, UUID)
    
    def test_two_default_uuids_are_different(self):
        flashcard1 = Flashcard()
        flashcard2 = Flashcard()
        self.assertEqual(flashcard1.id, flashcard1.id)
        self.assertNotEqual(flashcard1.id, flashcard2.id)

    def test_given_uuid(self):
        id_ = uuid4()
        new_flashcard = Flashcard(id_=id_)
        self.assertIsInstance(new_flashcard.id, UUID)
        self.assertEqual(new_flashcard.id, id_)