class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        # Sort the original word for comparison
        sorted_word = sorted(self.word.lower())
        matches = []

        for candidate in word_list:
            if sorted(candidate.lower()) == sorted_word and candidate.lower() != self.word.lower():
                matches.append(candidate)

        return matches
