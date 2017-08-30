from mathsmaps.flashcard import Flashcard

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
        self.name = name
        self.flashcards = {}

        for id_ in flashcard_dicts:
            if "id_" in flashcard_dicts[id_]:
                self.flashcards[id_] = Flashcard(**flashcard_dicts[id_])
            else:
                self.flashcards[id_] = Flashcard(id_=id_, **flashcard_dicts[id_])
        
        self.make_links(links)
    
    def make_links(self, links):
        """
        Given a list of links in the form (lowerUUID, upperUUID)
        Adds these links to the flashcards in the MathsMap.
        """
        for lower_id, upper_id in links:
            lower = self.flashcards[lower_id]
            upper = self.flashcards[upper_id]
            self.add_link(lower, upper)
    
    def add_link(self, lower_flashcard, upper_flashcard):
        """
        Given a lower and upper flashcard, add a link between them.
        """
        lower_flashcard.upper_links.append(upper_flashcard)
        upper_flashcard.lower_links.append(lower_flashcard)

    def add_card(self, flashcard_dict):
        """
        Add a new card to the map of flashcards, returning the card created.
        """
        card = Flashcard(**flashcard_dict)
        self.flashcards[card.id] = card
        return card
   
    def make_save_dict(self):
        """
        Makes a pickleable dictionary to save the MathsMap
        """
        pass