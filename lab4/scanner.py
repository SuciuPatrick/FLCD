import re


class Scanner:
    def __init__(self, pif, symbol_table, filename):
        self.pif = pif
        self.symbol_table = symbol_table
        self.filename = filename

    def detect(self, line):
        tokens = re.split('([^a-zA-Z0-9\!\=\*\-\+\"\'])', line)
        tokens = list(filter(lambda x: x != " " and x != "" and x != "\n" and x != "\t", tokens))
        return tokens

    def is_operator(self, token):
        token = re.match(r'[\\\+\-\*!=<>]=|and|or|not|[+-><=/*]', token)
        if token:
            return token

    # check for words like intANA
    def is_reserved_keyword(self, token):
        token = re.match(r'integer|bool|char|list|if|else|for|while|print', token)
        if token:
            return token

    def is_separator(self, token):
        token = re.match(r'[\[\],\.:\{\}\(\)]', token)
        if token:
            return token

    def is_identifier(self, token):
        token = re.match(r'^[a-zA-Z_]+[0-9a-zA-Z_]*$', token)
        if token:
            return token

    def is_constant(self, token):
        token = re.match(f"^0|[+-]?[1-9]{1}[0-9]*$", token) or re.match("[\"\\'][a-zA-Z0-9]+[\\'\"]$", token)
        if token:
            return token

    def print_file_pif(self):
        with open('pif_out.txt', 'w') as f:
            for elem in self.pif.elems:
                f.write(str(elem) + '\n')

    def print_file_symbol_table(self):
        with open('symbol_table.txt', 'w') as f:
            for elem in self.symbol_table.elems:
                f.write(str(elem) + '\n')

    def scan(self):
        with open(self.filename) as f:
            for line in f:
                tokens = self.detect(line)
                for token in tokens:
                    token.strip()
                    if self.is_reserved_keyword(token) or self.is_separator(token) or self.is_operator(token):
                        self.pif.add(token, 0)
                    elif self.is_identifier(token) or self.is_constant(token):
                        index = self.symbol_table.insert(token)
                        self.pif.add(token, index)
                    else:
                        print(f"{token} -> Lexical error")

        self.print_file_pif()
        self.print_file_symbol_table()
