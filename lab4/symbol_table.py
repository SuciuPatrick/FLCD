
class SymbolTable(dict):
    elems = []

    def tokens(self):
        return self.values()

    def insert(self, name):
        if name in self.elems:
            return self.elems.index(name)
        self.elems.append(name)
        return self.elems.index(name)

    def __str__(self):
        return "\n".join(str(token) for token in self.tokens())

#
# table = SymbolTable()
# table.insert('+', 0)
# table.insert(3, 1)
# table.insert(3, 5)
# table.insert('a', 10)
# table.insert('-', 0)
# table.insert('c', 3)
# table.insert('d', 4)
# print(table.position('a'))
#
# print(table)
#
# print(table.position(3))
