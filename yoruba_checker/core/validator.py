from typing import Tuple
from core.tokenizer import Tokenizer
from core.parser import CFGParser

class SentenceValidator:
    def __init__(self, grammar_path: str):
        self.tokenizer = Tokenizer()
        self.parser = CFGParser(grammar_path)

    def validate(self, sentence: str) -> Tuple[bool, str]:
        tokens = self.tokenizer.tokenize(sentence)
        parses = self.parser.parse(tokens)

        if parses:
            return True, "Valid Yorùbá sentence based on grammar rules."
        return False, "Invalid Yorùbá sentence. Grammar rules violated."
