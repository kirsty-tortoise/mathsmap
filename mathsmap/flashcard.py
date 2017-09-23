from uuid import uuid4

class Flashcard(object):
    """
    Flashcard class for flashcards which can be connected into maps.
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

        self.upper_links = []
        self.lower_links = []

    def make_save_dict(self):
        return dict(id_=self.id,
                    title=self.title,
                    text=self.text,
                    )