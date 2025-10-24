class MagicDictionary:

    def __init__(self):
        self.words = []

    def buildDict(self, dictionary: list[str]) -> None:
        self.words = dictionary

    def search(self, searchWord: str) -> bool:
        for word in self.words:
            if len(word) != len(searchWord):
                continue

            difference = 0
            for a, b in zip(word, searchWord):
                if a != b:
                    difference += 1
                if difference > 1:
                    break

            if difference == 1:
                return True

        return False
