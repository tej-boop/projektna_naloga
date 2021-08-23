class Word:
    def __init__(self, text, language, difficulty, type, gender=None, favourited=False):
        self.text = text
        self.language = language
        self.difficulty = difficulty
        self.type = type
        self.gender = gender
        self.favourited = favourited

    def toggle_favourite(self):
        self.favourited = not self.favourited

class Noun(Word):
    nouns = []

    def __init__(self, *args):
        Word.__init__(self, *args)
        self.nouns.append(self)
    
class Adjective(Word):
    adjectives = []

    def __init__(self, *args):
        Word.__init__(self, *args)
        self.adjectives.append(self)

class Insult:
    def __init__(self, adjective, noun, favourited=False):
        self.adjective = adjective
        self.noun = noun
        self.favourited = favourited

    def toggle_favourite(self):
        self.favourited = not self.favourited
