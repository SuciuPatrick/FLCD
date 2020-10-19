class Token:
    def __init__(self, name):
        self.name = name
        self.lines = []

    def add_line(self, line):
        self.lines.append(line)

    def __str__(self):
        lines_as_str = ', '.join('%d' % line for line in self.lines)
        return "%s: %s" % (self.name, lines_as_str)


class SymbolTable(dict):
    def tokens(self):
        return self.values()

    def position(self, name):
        return self.get(name) or self.setdefault(name, Token(name))

    def insert(self, name, line):
        if self.position(name):  # if already exists, we return pos
            return self.get(name)
        self.position(name).add_line(line)

    def __str__(self):
        return "\n".join(str(token) for token in self.tokens())


table = SymbolTable()
table.insert('+', 0)
table.insert(3, 1)
table.insert(3, 5)
table.insert('a', 10)
table.insert('-', 0)
table.insert('c', 3)
table.insert('d', 4)
print(table.position('a'))

print(table)

print(table.position(3))
