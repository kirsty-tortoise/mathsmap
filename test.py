import unittest
from flashcards import MathsMap, Flashcard

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

class TestMathsMap(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()