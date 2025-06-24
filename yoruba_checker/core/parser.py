import nltk
nltk.download('punkt_tab')

class CFGParser:
    def __init__(self, grammar_path: str):
        with open(grammar_path, 'r', encoding='utf-8') as file:
            grammar = nltk.CFG.fromstring(file.read())
        self.parser = nltk.ChartParser(grammar)

    def parse(self, tokens):
        try:
            return list(self.parser.parse(tokens))
        except ValueError:
            return None
