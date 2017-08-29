class Flashcard(object):
    def __init__(self, flashcard_dict):
        if "title" in flashcard_dict:
            self.title = flashcard_dict["title"]
        else:
            self.title = "Untitled"

        if "text" in flashcard_dict:
            self.text = flashcard_dict["text"]
        else:
            self.text = ""

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