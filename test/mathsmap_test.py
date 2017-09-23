import unittest
from uuid import uuid4, UUID
from pickle import dumps, loads
from mathsmap.mathsmap import MathsMap

class TestMathsMap(unittest.TestCase):
    def test_make_empty_mathsmap(self):
        new_map = MathsMap(name="Empty")
        self.assertEqual(new_map.name, "Empty")
        self.assertEqual(new_map.flashcards, {})

    def test_make_single_flashcard_mathsmap(self):
        id_ = uuid4()
        flashcard_dicts = {id_: dict(id_=id_, title="Lonely")}
        new_map = MathsMap(name="One Card!", flashcard_dicts=flashcard_dicts)
        self.assertEqual(len(new_map.flashcards), 1)
        self.assertEqual(new_map.flashcards[id_].title, "Lonely")
        self.assertEqual(new_map.flashcards[id_].id, id_)

    def test_make_many_flashcards_mathsmap(self):
        cards = {}
        for i in range(100):
            id_ = uuid4()
            cards[id_] = dict(id_=id_, title="Duplicate")
        special_id = uuid4()
        cards[special_id] = dict(id_=special_id, title="SPECIAL!!!")
        new_map = MathsMap(name="Large Map!", flashcard_dicts=cards)
        self.assertEqual(len(new_map.flashcards), 101)
        self.assertEqual(new_map.flashcards[special_id].id, special_id)
        self.assertEqual(new_map.flashcards[special_id].title, "SPECIAL!!!")
    
    def test_flashcards_without_id_given(self):
        id_ = uuid4()
        new_map = MathsMap(name="A map", flashcard_dicts={id_:{"title":"A card"}})
        self.assertEqual(new_map.flashcards[id_].id, id_)
    
    def test_mathsmap_with_two_cards_and_single_link(self):
        id1, id2 = uuid4(), uuid4()
        card1 = dict(id_=id1, title="CARD1")
        card2 = dict(id_=id2, title="CARD2")
        new_map = MathsMap(name="Two cards", flashcard_dicts={id1:card1, id2:card2}, links=[(id1,id2)])
        c1, c2 = new_map.flashcards[id1], new_map.flashcards[id2]
        self.assertTrue(is_linked(c1,c2))
        self.assertTrue(is_not_linked(c2,c1))
    
    def test_mathsmap_with_two_cards_and_double_link(self):
        id1, id2 = uuid4(), uuid4()
        card1 = dict(id_=id1, title="CARD1")
        card2 = dict(id_=id2, title="CARD2")
        new_map = MathsMap(name="Two cards", flashcard_dicts={id1:card1, id2:card2}, links=[(id1,id2), (id2,id1)])
        c1, c2 = new_map.flashcards[id1], new_map.flashcards[id2]
        self.assertTrue(is_linked(c1,c2))
        self.assertTrue(is_linked(c2,c1))

    def test_mathsmap_with_three_cards_and_a_link(self):
        id1, id2, id3 = uuid4(), uuid4(), uuid4()
        card1 = dict(id_=id1, title="CARD1")
        card2 = dict(id_=id2, title="CARD2")
        card3 = dict(id_=id3, title="CARD3")
        new_map = MathsMap(name="Three cards", flashcard_dicts={id1:card1, id2:card2, id3:card3}, links=[(id1,id2)])
        c1, c2, c3 = new_map.flashcards[id1], new_map.flashcards[id2], new_map.flashcards[id3]
        self.assertTrue(is_linked(c1,c2))
        self.assertTrue(is_not_linked(c2,c1))
        self.assertTrue(is_not_linked(c1,c3))
        self.assertTrue(is_not_linked(c3,c2))
    
    def test_mathsmap_with_many_cards_and_many_links(self):
        ids = []
        cards = {}
        for i in range(20):
            id_ = uuid4()
            ids.append(id_)
            cards[id_] = dict(id_=id_, title="CARD")
        links = []
        for i in range(19):
            links.append((ids[i], ids[i+1]))
        map_ = MathsMap(name="Many cards", flashcard_dicts=cards, links=links)
        c10, c11, c12 = map_.flashcards[ids[10]], map_.flashcards[ids[11]], map_.flashcards[ids[12]]
        self.assertTrue(is_linked(c10,c11))
        self.assertTrue(is_linked(c11,c12))
        self.assertTrue(is_not_linked(c10,c12))
        self.assertTrue(is_not_linked(c11,c10))
    
    def test_add_link_between_two_cards(self):
        id1, id2 = uuid4(), uuid4()
        new_map = MathsMap(name="Two cards", flashcard_dicts={id1:{}, id2:{}})
        card1, card2 = new_map.flashcards[id1], new_map.flashcards[id2]
        self.assertTrue(is_not_linked(card1, card2))
        self.assertTrue(is_not_linked(card2, card1))
        new_map.add_link(card1, card2)
        self.assertTrue(is_linked(card1, card2))
        self.assertTrue(is_not_linked(card2, card1))
    
    def test_add_card_without_id(self):
        new_map = MathsMap(name="Empty")
        card = new_map.add_card(title="A new card!", text="This card is new")
        self.assertIsInstance(card.id, UUID)
        self.assertEqual(card.title, "A new card!")
        self.assertEqual(card.text, "This card is new")
        self.assertEqual(len(new_map.flashcards), 1)
        self.assertIn(card, new_map.flashcards.values())
        self.assertEqual(new_map.flashcards[card.id], card)
    
    def test_add_card_with_id(self):
        new_map = MathsMap(name="Empty")
        id_ = uuid4()
        card = new_map.add_card(id_=id_)
        self.assertEqual(id_, card.id)
        self.assertEqual(new_map.flashcards[id_], card)
    
    def test_add_card_to_map_with_cards(self):
        id1, id2 = uuid4(), uuid4()
        new_map = MathsMap(name="Only one for now", flashcard_dicts={id1:dict(title="The first card")})
        self.assertEqual(len(new_map.flashcards), 1)
        card = new_map.add_card(id_=id2, title="The second card")
        self.assertEqual(len(new_map.flashcards), 2)
        self.assertEqual(card, new_map.flashcards[id2])
    
    def test_add_two_cards(self):
        new_map = MathsMap(name="Two to add")
        card1 = new_map.add_card(title="The first card")
        card2 = new_map.add_card(title="The second card")
        self.assertNotEqual(card1.id, card2.id)
        self.assertIn(card1, new_map.flashcards.values())
        self.assertIn(card2, new_map.flashcards.values())
        self.assertEqual(len(new_map.flashcards), 2)
    
    def test_save_and_pickle_empty_map(self):
        original_map = MathsMap(name="Empty map")
        saved = dumps(original_map.make_save_dict())
        new_map = MathsMap(**loads(saved))
        self.assertEqual(new_map.name, original_map.name)
        self.assertEqual(len(new_map.flashcards), 0)
    
    def test_save_and_pickle_map_without_links(self):
        original_map = MathsMap(name="Big Map")
        for i in range(20):
            original_map.add_card(title=str(i), text="This is a great card " + str(i))
        new_map = MathsMap(**loads(dumps(original_map.make_save_dict())))
        self.assertEqual(original_map.name, new_map.name)
        self.assertEqual(len(original_map.flashcards), len(new_map.flashcards))
        for id_,original_card in original_map.flashcards.items():
            new_card = new_map.flashcards[id_]
            for key in ["title", "text", "id"]:
                self.assertEqual(getattr(new_card, key), getattr(original_card, key))
    
    def test_save_and_pickle_links(self):
        original_map = MathsMap(name="Two cards")
        card1 = original_map.add_card(title="CARD1")
        card2 = original_map.add_card(title="CARD2")
        original_map.add_link(card1, card2)
        new_map = MathsMap(**loads(dumps(original_map.make_save_dict())))
        new_card1, new_card2 = new_map.flashcards[card1.id], new_map.flashcards[card2.id]
        self.assertTrue(is_linked(new_card1, new_card2))
        self.assertTrue(is_not_linked(new_card2, new_card1))

    def test_mathsmaps_do_not_interfere(self):
        mathsmap1 = MathsMap(name="Map1")
        mathsmap2 = MathsMap(name="Map2")
        card = mathsmap1.add_card()
        self.assertIn(card, mathsmap1.flashcards.values())
        self.assertNotIn(card, mathsmap2.flashcards.values())
        self.assertEqual(len(mathsmap2.flashcards), 0)

def is_linked(lower, upper):
    return (lower in upper.lower_links 
        and upper in lower.upper_links)

def is_not_linked(lower, upper):
    return (not lower in upper.lower_links
        and not upper in lower.upper_links)

if __name__ == "__main__":
    unittest.main()