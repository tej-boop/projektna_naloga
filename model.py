import random
import glob

class Word:
    def __init__(self, text, language, difficulty, gender):
        self.text = text
        self.language = language
        self.difficulty = difficulty
        self.gender = gender
        self.favourited = False

    def __str__(self):
        return self.text

    def toggle_favourite(self):
        self.favourited = not self.favourited

    @staticmethod
    def load_from_file(file):
        filedata = file[24:-4]
        language, difficulty, gender, type = filedata.split("_")
        with open(file, encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if type == "adj":
                    Adjective(line, language, difficulty, gender)
                if type == "noun":
                    Noun(line, language, difficulty, gender)
    
    @staticmethod
    def parse():
        for file in glob.glob("projektna_naloga/besede/*.txt"):
            Word.load_from_file(file)
            #print(file)

class Noun(Word):
    nouns = []

    def __init__(self, *args):
        Word.__init__(self, *args)
        if not any([self.text == other.text and self.difficulty == other.difficulty for other in self.nouns]):
            self.nouns.append(self)
    
class Adjective(Word):
    adjectives = []

    def __init__(self, *args):
        Word.__init__(self, *args)
        if not any([self.text == other.text and self.difficulty == other.difficulty for other in self.adjectives]):
            self.adjectives.append(self)

class Insult:
    def __init__(self, adjective, noun):
        self.adjective = adjective
        self.noun = noun
        self.favourited = False

    def __str__(self):
        if self.noun.language == "en":
            return f"{self.adjective} {self.noun}"
        if self.noun.language == "si":
            return f"{self.noun} {self.adjective}"

    def toggle_favourite(self):
        self.favourited = not self.favourited

    @staticmethod
    def generate(language, difficulty, gender):
        long_noun_list = [x for x in Noun.nouns if language == x.language and difficulty == x.difficulty and gender == x.gender]
        if len(long_noun_list) != 0:
            noun = random.choice(long_noun_list)
            long_adjective_list = [x for x in Adjective.adjectives if language == x.language and difficulty == x.difficulty and gender == x.gender and gender == noun.gender]
            if len(long_adjective_list) != 0:
                adjective = random.choice(long_adjective_list)
            return Insult(adjective, noun)
        elif len(long_noun_list) == 0:
            return Insult("Not enough", "Data")

if __name__ == "__main__":
    Word.parse()
    while True:
        lan = input("Enter a language: ")
        diff = input("Pick a difficulty (baby/hardcore): ")
        if lan == "si":
            gen = input("Pick a gender (f/m/t): ")
            print(Insult.generate(lan, diff, gen))
        if lan == "en":
            print(Insult.generate(lan, diff, "x"))