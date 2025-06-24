import nltk
nltk.download('punkt_tab')
from typing import List

class Tokenizer:
    def __init__(self):
        pass

    def tokenize(self, sentence: str) -> List[str]:
        return nltk.word_tokenize(sentence.lower())
