class Flashcard(object):
    def __init__(self, title="Untitled", text="", **kwargs):
        """
        Create a Flashcard with a title and text.
        Should only be used by MathsMap and similar.
        """
        self.title = title
        self.text = text

class MathsMap(object):
    def __init__(self, flashcards_dict):
        pass
    
    def make_links(self):
        pass

    def add_card(self, flashcard_dict):
        pass
    
    def remove_card(self, name):
        pass
   
    def count_cards(self):
        pass

    def make_save_dict(self):
        pass