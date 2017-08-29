from uuid import uuid4

class Flashcard(object):
    """
    Flashcard object connected into maps
    """

    def __init__(self, title="Untitled", text="", id_=None,  **kwargs):
        """
        Create a Flashcard with a title and text.
        Should only be used by MathsMap and similar.
        Arguments: title - String, Title of card, default Untitled 
                   text - String, Text on card, default empty
                   id_ - UUID object, default is to get a new uuid
                   **kwargs - Extra arguments are ignored
        """
        self.title = title
        self.text = text
        if id_ is None:
            self.id = uuid4()
        else:
            self.id = id_

class MathsMap(object):
    """
    """
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