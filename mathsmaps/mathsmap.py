class MathsMap(object):
    """
    Map class for maps which will be made up of flashcards.
    """
    def __init__(self, name, flashcard_dicts={}, links=[]):
        """
        Creates a MathsMap given a dictiionary of flashcards each in dictionary form and a list of links.
        Arguments: name - String  name for the mathsmap
                   flashcards_dict - Dictionary of flashcard dictionaries by id
                   links - List of links between flashcards, in the form (lowerUUID, upperUUID)
        """
        pass
    
    def make_links(self, links):
        """
        Given a list of links in the form (lowerUUID, upperUUID)
        Adds these links to the flashcards in the MathsMap.
        """
        pass
    
    def add_link(self, lower_flashcard, upper_flashcard):
        """
        Given a lower and upper flashcard, add a link between them.
        """
        pass

    def add_card(self, flashcard_dict):
        """
        Add a new card to the map of flashcards.
        """
        pass
    
    def remove_card(self, name):
        """
        Remove a card from the map of flashcards
        """
        pass
   
    def count_cards(self):
        """
        Counts cards in the map.
        """
        pass

    def make_save_dict(self):
        """
        Makes a pickleable dictionary to save the MathsMap
        """
        pass